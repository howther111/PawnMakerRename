import re
import time
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


APP_TITLE = "アルシャードセイヴァー キャラクターシート抽出"

DEFAULT_URL = (
    ""
)


def clean_text(text):
    """余分な空白・改行を整理する。"""
    if text is None:
        return ""

    text = str(text)
    text = text.replace("\u00a0", " ")
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def escape_markdown_cell(text):
    """Markdown表のセル用に文字列を整える。"""
    text = clean_text(text)
    text = text.replace("|", "｜")
    text = text.replace("\n", " / ")
    return text


def start_driver():
    """
    Chromeを起動する。

    Selenium 4.6以降では Selenium Manager により、
    ChromeDriver は原則自動管理される。
    """
    options = Options()

    # ブラウザ画面を表示しない
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")

    return webdriver.Chrome(options=options)


def wait_for_page(driver):
    """ページ読み込み完了を待つ。"""
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # JavaScriptによるフォーム値反映待ち
    time.sleep(2)


def extract_page_data(driver):
    """
    input / textarea / select の現在値を取得しながら、
    見出しや表を抽出する。
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

    function getControlValue(el) {
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
                return el.checked ? "ON" : "";
            }

            if (type === "radio") {
                if (!el.checked) {
                    return "";
                }

                return el.value || "選択";
            }

            return el.value || "";
        }

        if (tag === "textarea") {
            return el.value || "";
        }

        if (tag === "select") {
            const options = Array.from(el.selectedOptions || []);

            return options
                .map(opt => cleanText(opt.textContent || opt.value))
                .filter(Boolean)
                .join(", ");
        }

        return "";
    }

    function getCellText(cell) {
        const clone = cell.cloneNode(true);

        const originalControls = cell.querySelectorAll(
            "input, textarea, select"
        );

        const cloneControls = clone.querySelectorAll(
            "input, textarea, select"
        );

        cloneControls.forEach((cloneControl, index) => {
            const original = originalControls[index];

            if (!original) {
                cloneControl.remove();
                return;
            }

            const value = getControlValue(original);

            if (value) {
                const span = document.createElement("span");
                span.textContent = value;
                cloneControl.replaceWith(span);
            } else {
                cloneControl.remove();
            }
        });

        clone.querySelectorAll(
            "button, script, style, noscript"
        ).forEach(el => el.remove());

        return cleanText(
            clone.innerText ||
            clone.textContent ||
            ""
        );
    }

    const result = {
        title: document.title || "",
        url: location.href,
        sections: [],
        standaloneControls: []
    };

    const elements = document.body.querySelectorAll(
        "h1, h2, h3, h4, h5, h6, legend, table"
    );

    let tableNumber = 0;

    elements.forEach(el => {
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
            const text = cleanText(
                el.innerText ||
                el.textContent ||
                ""
            );

            if (text) {
                result.sections.push({
                    type: "heading",
                    level: tag === "legend" ? 2 : parseInt(tag.substring(1)),
                    text: text
                });
            }

            return;
        }

        if (tag === "table") {
            const rows = [];

            el.querySelectorAll(
                ":scope > tbody > tr, :scope > tr"
            ).forEach(tr => {
                const cells = [];

                tr.querySelectorAll(
                    ":scope > th, :scope > td"
                ).forEach(td => {
                    cells.push(getCellText(td));
                });

                if (cells.some(value => value !== "")) {
                    rows.push(cells);
                }
            });

            if (rows.length > 0) {
                tableNumber++;

                result.sections.push({
                    type: "table",
                    number: tableNumber,
                    rows: rows
                });
            }
        }
    });

    document.body.querySelectorAll(
        "input, textarea, select"
    ).forEach(el => {
        // 表内はすでに取得済み
        if (el.closest("table")) {
            return;
        }

        const value = getControlValue(el);

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
                    lab.innerText ||
                    lab.textContent ||
                    ""
                );
            }
        }

        if (!label && el.name) {
            label = el.name;
        }

        if (!label && el.id) {
            label = el.id;
        }

        result.standaloneControls.push({
            label: label,
            value: value
        });
    });

    return result;
    """

    return driver.execute_script(script)


def table_to_markdown(rows):
    """HTML表の抽出結果をMarkdown風テーブルに変換する。"""
    if not rows:
        return ""

    max_cols = max(len(row) for row in rows)
    normalized = []

    for row in rows:
        row = list(row)

        while len(row) < max_cols:
            row.append("")

        normalized.append(
            [escape_markdown_cell(value) for value in row]
        )

    if max_cols == 1:
        result = []

        for row in normalized:
            if row[0]:
                result.append(row[0])

        return "\n".join(result)

    output = []
    first = normalized[0]

    output.append("| " + " | ".join(first) + " |")
    output.append("| " + " | ".join(["---"] * max_cols) + " |")

    for row in normalized[1:]:
        output.append("| " + " | ".join(row) + " |")

    return "\n".join(output)


def make_llm_text(data):
    """Gemini / ChatGPT等に渡しやすいテキストを生成する。"""
    output = []

    output.append("# アルシャードセイヴァーRPG キャラクターシート")
    output.append("")

    if data.get("title"):
        output.append(
            "ページタイトル: " + clean_text(data["title"])
        )

    if data.get("url"):
        output.append(
            "取得元URL: " + clean_text(data["url"])
        )

    output.append("")
    output.append(
        "以下はアルシャードセイヴァーRPGの"
        "キャラクターシートから抽出した情報です。"
    )
    output.append(
        "フォームに入力・選択されている現在値を取得しています。"
    )
    output.append("")

    last_heading = ""

    for section in data.get("sections", []):
        if section["type"] == "heading":
            text = clean_text(section["text"])

            if not text:
                continue

            if text == last_heading:
                continue

            last_heading = text
            level = section.get("level", 2)
            level = max(2, min(level + 1, 5))

            output.append("#" * level + " " + text)
            output.append("")

        elif section["type"] == "table":
            rows = section.get("rows", [])

            if not rows:
                continue

            table_text = table_to_markdown(rows)

            if table_text:
                output.append(table_text)
                output.append("")

    controls = data.get("standaloneControls", [])

    if controls:
        output.append("## その他の入力情報")
        output.append("")

        for item in controls:
            label = clean_text(item.get("label", ""))
            value = clean_text(item.get("value", ""))

            if not value:
                continue

            if label:
                output.append(f"- {label}: {value}")
            else:
                output.append(f"- {value}")

        output.append("")

    text = "\n".join(output)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip() + "\n"


def export_character_sheet(url, output_path):
    """指定URLを読み込み、TXTへ保存する。"""
    driver = None

    try:
        driver = start_driver()
        driver.get(url)
        wait_for_page(driver)

        data = extract_page_data(driver)
        text = make_llm_text(data)

        # Windowsのメモ帳でも文字化けしにくいUTF-8 BOM付き
        with open(output_path, "w", encoding="utf-8-sig") as file:
            file.write(text)

        return data

    finally:
        if driver:
            driver.quit()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry("760x340")
        self.minsize(650, 300)

        self.create_widgets()

    def create_widgets(self):
        main = ttk.Frame(self, padding=20)
        main.pack(fill="both", expand=True)

        ttk.Label(
            main,
            text="キャラクターシートURL",
            font=("", 11, "bold")
        ).pack(anchor="w")

        self.url_var = tk.StringVar(value=DEFAULT_URL)

        self.url_entry = ttk.Entry(
            main,
            textvariable=self.url_var
        )
        self.url_entry.pack(fill="x", pady=(5, 15))

        ttk.Label(
            main,
            text=(
                "character-sheets.appspot.com の"
                "アルシャードセイヴァーRPG"
                "キャラクターシートを読み込み、"
                "Gemini・ChatGPT等の言語モデルが"
                "読み取りやすいテキスト形式に変換します。"
            ),
            wraplength=700
        ).pack(anchor="w", pady=(0, 20))

        self.run_button = ttk.Button(
            main,
            text="キャラクター情報を取得してTXT保存",
            command=self.run_export
        )
        self.run_button.pack(ipadx=10, ipady=8)

        self.status_var = tk.StringVar(value="待機中")

        ttk.Label(
            main,
            textvariable=self.status_var
        ).pack(pady=(20, 0))

    def run_export(self):
        url = self.url_var.get().strip()

        if not url:
            messagebox.showerror(
                APP_TITLE,
                "URLを入力してください。"
            )
            return

        if "character-sheets.appspot.com/al2/" not in url:
            result = messagebox.askyesno(
                APP_TITLE,
                (
                    "アルシャードセイヴァーのURLでは"
                    "ない可能性があります。\n\n"
                    "そのまま実行しますか？"
                )
            )

            if not result:
                return

        output_path = filedialog.asksaveasfilename(
            title="保存先を指定",
            defaultextension=".txt",
            filetypes=[
                ("テキストファイル", "*.txt"),
                ("すべてのファイル", "*.*")
            ],
            initialfile="alshard_savior_character.txt"
        )

        if not output_path:
            return

        self.run_button.config(state="disabled")
        self.status_var.set("キャラクターシートを読み込み中...")
        self.update()

        try:
            export_character_sheet(url, output_path)

            self.status_var.set("保存完了")

            messagebox.showinfo(
                APP_TITLE,
                (
                    "キャラクター情報を保存しました。\n\n"
                    + output_path
                )
            )

        except Exception as exc:
            self.status_var.set("エラー")

            messagebox.showerror(
                APP_TITLE,
                (
                    "処理中にエラーが発生しました。\n\n"
                    f"{type(exc).__name__}\n"
                    f"{exc}"
                )
            )

        finally:
            self.run_button.config(state="normal")


if __name__ == "__main__":
    app = App()
    app.mainloop()
