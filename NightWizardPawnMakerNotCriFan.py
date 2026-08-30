#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
import tkinter.messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


def none_to_str(value):
    if value is None:
        return ""
    else:
        return str(value)


class NightWizardData():
    url = ""
    base_memo = ""
    character_name = ""
    shuzoku = ""
    kinryoku = 0
    kiyou = 0
    kankaku = 0
    richi = 0
    ishi = 0
    kouun = 0
    taikyu = 0
    mahou = 0
    naihou = 0
    cf = 0
    koudou = 0
    meichu = 0
    madou = 0
    kaihi = 0
    butsukou = 0
    butsubou = 0
    makou = 0
    mabou = 0


    def input_data(self, driver, input_url):
        self.url = input_url
        self.base_memo = driver.find_element(by=By.NAME, value="pc_making_memo").get_attribute("value")
        self.character_name = driver.find_element(by=By.ID, value="pc_name").get_attribute("value")
        self.shuzoku = driver.find_element(by=By.ID, value="shuzoku").get_attribute("value")
        self.kinryoku = driver.find_element(by=By.ID, value="NP1").get_attribute("value")
        self.kiyou = driver.find_element(by=By.ID, value="NP2").get_attribute("value")
        self.kankaku = driver.find_element(by=By.ID, value="NP3").get_attribute("value")
        self.richi = driver.find_element(by=By.ID, value="NP4").get_attribute("value")
        self.ishi = driver.find_element(by=By.ID, value="NP5").get_attribute("value")
        self.kouun = driver.find_element(by=By.ID, value="NP6").get_attribute("value")
        self.taikyu = driver.find_element(by=By.ID, value="NP7").get_attribute("value")
        self.mahou = driver.find_element(by=By.ID, value="NP8").get_attribute("value")
        self.naihou = driver.find_element(by=By.ID, value="NP9").get_attribute("value")
        self.cf = driver.find_element(by=By.ID, value="NP10").get_attribute("value")
        self.koudou = driver.find_element(by=By.NAME, value="BSUM1").get_attribute("value")
        self.meichu = driver.find_element(by=By.NAME, value="BSUM2").get_attribute("value")
        self.madou = driver.find_element(by=By.NAME, value="BSUM3").get_attribute("value")
        self.kaihi = driver.find_element(by=By.NAME, value="BSUM4").get_attribute("value")
        self.butsukou = driver.find_element(by=By.NAME, value="BSUM5").get_attribute("value")
        self.butsubou = driver.find_element(by=By.NAME, value="BSUM6").get_attribute("value")
        self.makou = driver.find_element(by=By.NAME, value="BSUM7").get_attribute("value")
        self.mabou = driver.find_element(by=By.NAME, value="BSUM8").get_attribute("value")

        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = ""

        print(text)

        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_神我狩テキストデータ.txt"

        #f = open(file_name, 'w', encoding="utf-8")
        #f.write(text)
        #f.close()

        print("神我狩テキストデータを生成しました")
        self.output_pawn(text)

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = self.koudou
        jsontext["data"]["status"] = []

        i = 0

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "耐久力"
        jsontext["data"]["status"][i]["value"] = int(self.taikyu)
        jsontext["data"]["status"][i]["max"] = int(self.taikyu)
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "魔法力"
        jsontext["data"]["status"][i]["value"] = int(self.mahou)
        jsontext["data"]["status"][i]["max"] = int(self.mahou)
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "プラーナ"
        jsontext["data"]["status"][i]["value"] = int(self.naihou)
        jsontext["data"]["status"][i]["max"] = int(self.naihou)
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "クリティカル値"
        jsontext["data"]["status"][i]["value"] = 12
        jsontext["data"]["status"][i]["max"] = 12
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "ファンブル値"
        jsontext["data"]["status"][i]["value"] = 2
        jsontext["data"]["status"][i]["max"] = 2
        i = i + 1

        jsontext["data"]["params"] = []

        j = 0

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "筋力"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kinryoku)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "器用"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kiyou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "感覚"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kankaku)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "理知"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.richi)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "幸運"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kouun)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "CF修正"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.cf)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "命中"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.meichu)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魔導"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.madou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "回避"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kaihi)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "物攻"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.butsukou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "物防"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.butsubou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魔攻"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.makou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魔防"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.mabou)
        j = j + 1


        command = "//判定\n" + \
                  "2D6+{筋力}+0 体力判定\n" + \
                  "2D6+{器用}+0 器用判定\n" + \
                  "2D6+{感覚}+0 感覚判定\n" + \
                  "2D6+{理知}+0 理知判定\n" + \
                  "2D6+{幸運}+0 幸運判定\n" + \
                  "2D6+{命中}+0 命中判定\n" + \
                  "2D6+{魔導}+0 魔導判定\n" + \
                  "2D6+{回避}+0 回避判定\n" + \
                  "2D6+{物攻}+0 物攻判定\n" + \
                  "2D6+{物防}+0 物防判定\n" + \
                  "2D6+{魔攻}+0 魔攻判定\n" + \
                  "2D6+{魔防}+0 魔防判定\n" + \
                  "\n//耐久力\n" + \
                  "C({耐久力}-0) 残り耐久力"

        jsontext["data"]["commands"] = command

        jsontext["data"]["externalUrl"] = self.url
        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_ウィザード駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as filedata:  # 第二引数：writableオプションを指定
            json.dump(jsontext, filedata, ensure_ascii=False)

        print("ウィザード駒データを生成しました")


def get_data(value):
    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    nightwizard = NightWizardData()
    time.sleep(5)

    nightwizard.input_data(driver, url)
    nightwizard.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"ナイトウィザード3rd ココフォリア用駒データ作成ツール")
    root.geometry("400x150")

    frame1 = tkinter.Frame(root, width=400, height=50)  # Label
    frame2 = tkinter.Frame(root, width=400, height=50)  # Button, Entry
    frame3 = tkinter.Frame(root, width=200, height=50)  # Button, Entry
    frame4 = tkinter.Frame(root, width=200, height=50)  # Button, Entry

    frame1.propagate(False)
    frame2.propagate(False)
    frame3.propagate(False)
    frame4.propagate(False)

    # Frameを配置（grid）
    frame1.grid(row=0, column=0, columnspan=2)
    frame2.grid(row=1, column=0, columnspan=2)
    frame3.grid(row=2, column=0)
    frame4.grid(row=2, column=1)

    # ラベル
    Static1 = tkinter.Label(frame1, text=u'キャラクターシートURL\nhttps://charasheet.vampire-blood.net/nw3_pc_making.html')
    Static1.pack()

    # エントリー
    EditBox = tkinter.Entry(frame2, width=50)
    EditBox.pack()

    Button1 = tkinter.Button(frame3, text=u'生成', command=lambda: [get_data(EditBox.get())])
    Button1.pack()

    # ボタン
    Button2 = tkinter.Button(frame4, text=u'終了', command=lambda: root.quit())
    Button2.pack()

    root.mainloop()