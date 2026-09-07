import os
import re
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


APP_TITLE = "メタリックガーディアン キャラクターシート抽出"
DEFAULT_URL = (
    ""
)


def clean_text(text):
    """余分な空白や改行を整理"""
    if text is None:
        return ""

    text = str(text)
    text = text.replace("\u00a0", " ")
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # 横方向の余分な空白を整理
    text = re.sub(r"[ \t]+", " ", text)

    # 空行が増えすぎないようにする
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def escape_markdown_cell(text):
    """Markdown表のセル用に文字を整理"""
    text = clean_text(text)
    text = text.replace("|", "｜")
    text = text.replace("\n", " / ")
    return text


def start_driver():
    """
    Chromeを起動。
    Selenium 4.6以降は Selenium Manager により
    ChromeDriverが自動管理される。
    """
    options = Options()

    # ブラウザ画面を表示したくない場合は有効にする
    options.add_argument("--headless=new")

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # 自動操作であることによる余計な影響を減らす
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    return driver


def wait_for_page(driver):
    """ページの読み込み完了を待つ"""
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script(
            "return document.readyState"
        ) == "complete"
    )

    # JavaScript側でフォーム値の反映が行われる可能性を考え少し待つ
    time.sleep(2)


def extract_page_data(driver):
    """
    ページのDOMから、
    見出し・通常テキスト・表・フォーム値を
    LLM向けに抽出する。

    JavaScript側でinput/select/textareaの現在値を直接取得する。
    """

    script = r"""
    function cleanText(text) {
        if (!text) return "";
        return text
            .replace(/\u00a0/g, " ")
            .replace(/[ \t]+/g, " ")
            .replace(/\n[ \t]+/g, "\n")
            .trim();
    }

    function controlValue(el) {
        const tag = el.tagName.toLowerCase();

        if (tag === "input") {
            const type = (el.type || "").toLowerCase();

            if (
                type === "button" ||
                type === "submit" ||
                type === "reset" ||
                type === "image" ||
                type === "hidden"
            ) {
                return "";
            }

            if (type === "checkbox") {
                return el.checked ? "ON" : "OFF";
            }

            if (type === "radio") {
                return el.checked ? (el.value || "選択") : "";
            }

            return el.value || "";
        }

        if (tag === "textarea") {
            return el.value || "";
        }

        if (tag === "select") {
            const selected = Array.from(el.selectedOptions || []);
            return selected
                .map(opt => cleanText(opt.textContent || opt.value))
                .filter(Boolean)
                .join(", ");
        }

        return "";
    }

    function cellText(cell) {
        const clone = cell.cloneNode(true);

        const originalControls = cell.querySelectorAll(
            "input, textarea, select"
        );

        const clonedControls = clone.querySelectorAll(
            "input, textarea, select"
        );

        clonedControls.forEach((cloneControl, index) => {
            const original = originalControls[index];

            if (!original) {
                cloneControl.remove();
                return;
            }

            const value = controlValue(original);

            if (value) {
                const span = document.createElement("span");
                span.textContent = value;
                cloneControl.replaceWith(span);
            } else {
                cloneControl.remove();
            }
        });

        // ボタン等は削除
        clone.querySelectorAll(
            "button, script, style, noscript"
        ).forEach(el => el.remove());

        return cleanText(clone.innerText || clone.textContent || "");
    }

    function isVisible(el) {
        const style = window.getComputedStyle(el);

        if (
            style.display === "none" ||
            style.visibility === "hidden"
        ) {
            return false;
        }

        // タブ内など高さ0でもデータが存在する場合があるため
        // display/visibilityだけを見る
        return true;
    }

    const result = {
        title: document.title || "",
        url: location.href,
        sections: []
    };

    const body = document.body;

    const elements = body.querySelectorAll(
        "h1, h2, h3, h4, h5, h6, legend, table"
    );

    let sectionNumber = 0;

    elements.forEach(el => {
        if (!isVisible(el)) {
            // 非表示タブにも重要情報がある場合があるので
            // tableについては取得を継続する
            if (el.tagName.toLowerCase() !== "table") {
                return;
            }
        }

        const tag = el.tagName.toLowerCase();

        if (
            tag === "h1" ||
            tag === "h2" ||
            tag === "h3" ||
            tag === "h4" ||
            tag === "h5" ||
            tag === "h6" ||
            tag === "legend"
        ) {
            const text = cleanText(el.innerText || el.textContent || "");

            if (text) {
                result.sections.push({
                    type: "heading",
                    level:
                        tag === "legend"
                            ? 2
                            : parseInt(tag.substring(1)),
                    text: text
                });
            }

            return;
        }

        if (tag === "table") {
            const rows = [];

            el.querySelectorAll(":scope > tbody > tr, :scope > tr").forEach(
                tr => {
                    const cells = [];

                    tr.querySelectorAll(":scope > th, :scope > td").forEach(
                        td => {
                            const text = cellText(td);

                            // 完全に空でも列位置維持のため追加
                            cells.push(text);
                        }
                    );

                    // 空行は捨てる
                    if (cells.some(v => v !== "")) {
                        rows.push(cells);
                    }
                }
            );

            if (rows.length > 0) {
                sectionNumber++;

                result.sections.push({
                    type: "table",
                    number: sectionNumber,
                    rows: rows
                });
            }
        }
    });

    /*
     * 表に入っていないtextarea等を拾う
     */
    const standaloneControls = [];

    body.querySelectorAll("input, textarea, select").forEach(el => {
        if (el.closest("table")) {
            return;
        }

        const value = controlValue(el);

        if (!value) {
            return;
        }

        let label = "";

        if (el.id) {
            const lab = document.querySelector(
                'label[for="' + CSS.escape(el.id) + '"]'
            );

            if (lab) {
                label = cleanText(
                    lab.innerText || lab.textContent || ""
                );
            }
        }

        if (!label && el.name) {
            label = el.name;
        }

        if (!label && el.id) {
            label = el.id;
        }

        standaloneControls.push({
            label: label,
            value: value
        });
    });

    result.standaloneControls = standaloneControls;

    return result;
    """

    return driver.execute_script(script)


def table_to_markdown(rows):
    """
    HTML表をLLM向けMarkdown風テキストへ変換
    """

    if not rows:
        return ""

    max_cols = max(len(row) for row in rows)

    normalized = []

    for row in rows:
        row = list(row)

        while len(row) < max_cols:
            row.append("")

        normalized.append(
            [escape_markdown_cell(v) for v in row]
        )

    output = []

    # 1列なら普通の行形式にする
    if max_cols == 1:
        for row in normalized:
            if row[0]:
                output.append(row[0])

        return "\n".join(output)

    # Markdown形式
    first = normalized[0]

    output.append(
        "| " + " | ".join(first) + " |"
    )

    output.append(
        "| " + " | ".join(["---"] * max_cols) + " |"
    )

    for row in normalized[1:]:
        output.append(
            "| " + " | ".join(row) + " |"
        )

    return "\n".join(output)


def make_llm_text(data):
    """
    Gemini / ChatGPT等へ投入しやすいテキストを作る
    """

    result = []

    result.append(
        "# メタリックガーディアンRPG キャラクターシート"
    )
    result.append("")

    if data.get("title"):
        result.append(
            f"ページタイトル: {clean_text(data['title'])}"
        )

    if data.get("url"):
        result.append(
            f"取得元URL: {clean_text(data['url'])}"
        )

    result.append("")
    result.append(
        "以下はキャラクターシートから抽出した情報です。"
    )
    result.append(
        "表内の値は、ブラウザ上で実際に選択・入力されている現在値です。"
    )
    result.append("")

    last_heading = ""

    for section in data.get("sections", []):

        if section["type"] == "heading":
            text = clean_text(section["text"])

            if not text:
                continue

            # 同じ見出しの連続を避ける
            if text == last_heading:
                continue

            last_heading = text

            level = section.get("level", 2)

            # 最上位でも ## から開始
            level = max(2, min(level + 1, 5))

            result.append(
                "#" * level + " " + text
            )
            result.append("")

        elif section["type"] == "table":

            rows = section.get("rows", [])

            if not rows:
                continue

            table_text = table_to_markdown(rows)

            if table_text:
                result.append(table_text)
                result.append("")

    controls = data.get("standaloneControls", [])

    if controls:
        result.append("## その他の入力情報")
        result.append("")

        for item in controls:
            label = clean_text(item.get("label", ""))
            value = clean_text(item.get("value", ""))

            if not value:
                continue

            if label:
                result.append(
                    f"- {label}: {value}"
                )
            else:
                result.append(
                    f"- {value}"
                )

        result.append("")

    text = "\n".join(result)

    # 空行整理
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() + "\n"


def guess_filename(data):
    """
    ページ情報からファイル名候補を作る
    """

    title = clean_text(data.get("title", ""))

    if not title:
        title = "character_sheet"

    # Windowsで使えない文字除去
    title = re.sub(
        r'[\\/:*?"<>|]',
        "_",
        title
    )

    title = title.strip(" .")

    if not title:
        title = "character_sheet"

    return title + ".txt"


def export_character_sheet(url, output_path):
    driver = None

    try:
        driver = start_driver()

        driver.get(url)

        wait_for_page(driver)

        data = extract_page_data(driver)

        text = make_llm_text(data)

        with open(
            output_path,
            "w",
            encoding="utf-8-sig"
        ) as f:
            f.write(text)

        return data

    finally:
        if driver:
            driver.quit()


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry("760x330")
        self.minsize(650, 300)

        self.create_widgets()

    def create_widgets(self):

        main = ttk.Frame(
            self,
            padding=20
        )

        main.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            main,
            text="キャラクターシートURL",
            font=("", 11, "bold")
        ).pack(
            anchor="w"
        )

        self.url_var = tk.StringVar(
            value=DEFAULT_URL
        )

        self.url_entry = ttk.Entry(
            main,
            textvariable=self.url_var
        )

        self.url_entry.pack(
            fill="x",
            pady=(5, 15)
        )

        ttk.Label(
            main,
            text=(
                "character-sheets.appspot.com の"
                "メタリックガーディアンRPG"
                "キャラクターシートを、"
                "Gemini等の言語モデル向けテキストに変換します。"
            ),
            wraplength=700
        ).pack(
            anchor="w",
            pady=(0, 20)
        )

        self.run_button = ttk.Button(
            main,
            text="キャラクター情報を取得してTXT保存",
            command=self.run_export
        )

        self.run_button.pack(
            ipadx=10,
            ipady=8
        )

        self.status_var = tk.StringVar(
            value="待機中"
        )

        ttk.Label(
            main,
            textvariable=self.status_var
        ).pack(
            pady=(20, 0)
        )

    def run_export(self):

        url = self.url_var.get().strip()

        if not url:
            messagebox.showerror(
                APP_TITLE,
                "URLを入力してください。"
            )
            return

        if "character-sheets.appspot.com/mgr/" not in url:
            result = messagebox.askyesno(
                APP_TITLE,
                (
                    "メタリックガーディアンのURLでは"
                    "ない可能性があります。\n\n"
                    "そのまま実行しますか？"
                )
            )

            if not result:
                return

        default_name = "metallic_guardian_character.txt"

        output_path = filedialog.asksaveasfilename(
            title="保存先を指定",
            defaultextension=".txt",
            filetypes=[
                ("テキストファイル", "*.txt"),
                ("すべてのファイル", "*.*")
            ],
            initialfile=default_name
        )

        if not output_path:
            return

        self.run_button.config(
            state="disabled"
        )

        self.status_var.set(
            "キャラクターシートを読み込み中..."
        )

        self.update()

        try:

            data = export_character_sheet(
                url,
                output_path
            )

            self.status_var.set(
                "保存完了"
            )

            messagebox.showinfo(
                APP_TITLE,
                (
                    "キャラクター情報を保存しました。\n\n"
                    f"{output_path}"
                )
            )

        except Exception as e:

            self.status_var.set(
                "エラー"
            )

            messagebox.showerror(
                APP_TITLE,
                (
                    "処理中にエラーが発生しました。\n\n"
                    f"{type(e).__name__}\n"
                    f"{e}"
                )
            )

        finally:

            self.run_button.config(
                state="normal"
            )


if __name__ == "__main__":
    app = App()
    app.mainloop()