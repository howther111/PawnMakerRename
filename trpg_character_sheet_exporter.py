import re
import time
import tkinter as tk
from urllib.parse import urlparse
from tkinter import ttk, messagebox, filedialog

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


APP_TITLE = "TRPG キャラクターシート AI用TXT出力"

SUPPORTED_SYSTEMS = {
    "mgr": {
        "name": "メタリックガーディアンRPG",
        "default_filename": "metallic_guardian_character.txt",
    },
    "al2": {
        "name": "アルシャードセイヴァーRPG",
        "default_filename": "alshard_savior_character.txt",
    },
    "tgs": {
        "name": "トワイライトガンスモーク",
        "default_filename": "twilight_gunsmoke_character.txt",
    },
}

DEFAULT_URL = (
    ""
)


def clean_text(text):
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
    text = clean_text(text)
    text = text.replace("|", "｜")
    text = text.replace("\n", " / ")
    return text


def detect_system(url):
    try:
        parsed = urlparse(url)
        path = parsed.path.lower()
    except Exception:
        return None, None

    for code, info in SUPPORTED_SYSTEMS.items():
        if f"/{code}/" in path:
            return code, info

    return None, None


def start_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    return webdriver.Chrome(options=options)


def wait_for_page(driver):
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    time.sleep(3)


def extract_page_data(driver):
    script = r"""
    function cleanText(text) {
        if (!text) return "";
        return String(text)
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
                type === "hidden" ||
                type === "file"
            ) {
                return "";
            }

            if (type === "checkbox") {
                return el.checked ? "ON" : "";
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

    function replaceControlsWithValues(root, originalRoot) {
        const originalControls = originalRoot.querySelectorAll(
            "input, textarea, select"
        );
        const cloneControls = root.querySelectorAll(
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
    }

    function getCellText(cell) {
        const clone = cell.cloneNode(true);
        replaceControlsWithValues(clone, cell);

        clone.querySelectorAll(
            "button, script, style, noscript"
        ).forEach(el => el.remove());

        return cleanText(
            clone.innerText ||
            clone.textContent ||
            ""
        );
    }

    function getElementTextWithControlValues(el) {
        const clone = el.cloneNode(true);
        replaceControlsWithValues(clone, el);

        clone.querySelectorAll(
            "button, script, style, noscript"
        ).forEach(node => node.remove());

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
            const text = getElementTextWithControlValues(el);

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

            Array.from(el.rows).forEach(tr => {
                const cells = [];

                Array.from(tr.cells).forEach(cell => {
                    cells.push(getCellText(cell));
                });

                if (cells.some(value => cleanText(value) !== "")) {
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
        if (el.closest("table")) {
            return;
        }

        const value = getControlValue(el);

        if (!value) {
            return;
        }

        let label = "";

        if (el.id) {
            try {
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
            } catch (e) {
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
        return "\n".join(
            row[0] for row in normalized if row[0]
        )

    output = []
    first = normalized[0]

    output.append("| " + " | ".join(first) + " |")
    output.append("| " + " | ".join(["---"] * max_cols) + " |")

    for row in normalized[1:]:
        output.append("| " + " | ".join(row) + " |")

    return "\n".join(output)


def make_llm_text(data, system_info):
    system_name = system_info["name"]

    output = [
        f"# {system_name} キャラクターシート",
        "",
    ]

    if data.get("title"):
        output.append("ページタイトル: " + clean_text(data["title"]))

    if data.get("url"):
        output.append("取得元URL: " + clean_text(data["url"]))

    output.extend([
        "",
        f"以下はTRPG『{system_name}』のキャラクターシートから抽出した情報です。",
        "フォームに入力・選択されている現在値、および合計・計算済みの行を含めて取得しています。",
        "",
    ])

    last_heading = ""

    for section in data.get("sections", []):
        if section["type"] == "heading":
            text = clean_text(section.get("text", ""))

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
    system_code, system_info = detect_system(url)

    if not system_info:
        raise ValueError(
            "対応していないURLです。\n\n"
            "対応システム:\n"
            "・メタリックガーディアンRPG（/mgr/）\n"
            "・アルシャードセイヴァーRPG（/al2/）\n"
            "・トワイライトガンスモーク（/tgs/）"
        )

    driver = None

    try:
        driver = start_driver()
        driver.get(url)
        wait_for_page(driver)

        data = extract_page_data(driver)
        text = make_llm_text(data, system_info)

        with open(
            output_path,
            "w",
            encoding="utf-8-sig"
        ) as file:
            file.write(text)

        return system_code, system_info, data

    finally:
        if driver:
            driver.quit()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(APP_TITLE)
        self.geometry("820x410")
        self.minsize(700, 360)

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
        self.url_entry.pack(fill="x", pady=(5, 8))

        self.system_var = tk.StringVar(
            value=(
                "対応：メタリックガーディアン / "
                "アルシャードセイヴァー / "
                "トワイライトガンスモーク"
            )
        )

        ttk.Label(
            main,
            textvariable=self.system_var
        ).pack(anchor="w", pady=(0, 15))

        ttk.Label(
            main,
            text=(
                "3種類の character-sheets.appspot.com のURLを自動判別し、"
                "キャラクター情報をGemini・ChatGPT等が読み取りやすい"
                "Markdown風TXTへ変換します。"
                "入力値だけでなく、表内の「合計」行や計算済みの数値も出力します。"
            ),
            wraplength=760
        ).pack(anchor="w", pady=(0, 20))

        self.url_var.trace_add("write", self.on_url_changed)

        self.run_button = ttk.Button(
            main,
            text="キャラクター情報を取得してTXT保存",
            command=self.run_export
        )
        self.run_button.pack(ipadx=12, ipady=8)

        self.status_var = tk.StringVar(value="待機中")

        ttk.Label(
            main,
            textvariable=self.status_var
        ).pack(pady=(20, 0))

    def on_url_changed(self, *args):
        url = self.url_var.get().strip()
        _, system_info = detect_system(url)

        if system_info:
            self.system_var.set(
                "判別されたシステム：" + system_info["name"]
            )
        else:
            self.system_var.set(
                "対応：メタリックガーディアン / "
                "アルシャードセイヴァー / "
                "トワイライトガンスモーク"
            )

    def run_export(self):
        url = self.url_var.get().strip()

        if not url:
            messagebox.showerror(
                APP_TITLE,
                "URLを入力してください。"
            )
            return

        _, system_info = detect_system(url)

        if not system_info:
            messagebox.showerror(
                APP_TITLE,
                (
                    "対応していないURLです。\n\n"
                    "対応システムは次の3種類です。\n"
                    "・メタリックガーディアンRPG\n"
                    "・アルシャードセイヴァーRPG\n"
                    "・トワイライトガンスモーク"
                )
            )
            return

        output_path = filedialog.asksaveasfilename(
            title="保存先を指定",
            defaultextension=".txt",
            filetypes=[
                ("テキストファイル", "*.txt"),
                ("すべてのファイル", "*.*"),
            ],
            initialfile=system_info["default_filename"]
        )

        if not output_path:
            return

        self.run_button.config(state="disabled")
        self.status_var.set(
            f"{system_info['name']} のキャラクターシートを読み込み中..."
        )
        self.update()

        try:
            _, system_info, _ = export_character_sheet(
                url,
                output_path
            )

            self.status_var.set("保存完了")

            messagebox.showinfo(
                APP_TITLE,
                (
                    f"{system_info['name']} のキャラクター情報を保存しました。\n\n"
                    f"{output_path}"
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
