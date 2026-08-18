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


class KamigakariData():
    url = ""
    base_memo = ""
    character_name = ""
    shuzoku = ""
    tairyoku = 0
    binshou = 0
    chisei = 0
    seishin = 0
    kouun = 0
    meichu = 0
    kaihi = 0
    hatsudou = 0
    teikou = 0
    kanpa = 0
    butsud = 0
    mad = 0
    koudou = 0
    seimei = 0
    idou = 0
    zenryokuidou = 0
    money = 0
    reiryoku_dice_max = 0
    reimon_max = 0

    def input_data(self, driver, input_url):
        self.url = input_url
        self.base_memo = driver.find_element(by=By.NAME, value="pc_making_memo").get_attribute("value")
        self.character_name = driver.find_element(by=By.ID, value="pc_name").get_attribute("value")
        self.shuzoku = driver.find_element(by=By.ID, value="SL_shuzoku").get_attribute("value")
        self.tairyoku = driver.find_element(by=By.ID, value="NB1").get_attribute("value")
        self.binshou = driver.find_element(by=By.ID, value="NB2").get_attribute("value")
        self.chisei = driver.find_element(by=By.ID, value="NB3").get_attribute("value")
        self.seishin = driver.find_element(by=By.ID, value="NB4").get_attribute("value")
        self.kouun = driver.find_element(by=By.ID, value="NB5").get_attribute("value")
        self.meichu = driver.find_element(by=By.ID, value="NP1").get_attribute("value")
        self.kaihi = driver.find_element(by=By.ID, value="NP2").get_attribute("value")
        self.hatsudou = driver.find_element(by=By.ID, value="NP3").get_attribute("value")
        self.teikou = driver.find_element(by=By.ID, value="NP4").get_attribute("value")
        self.kanpa = driver.find_element(by=By.ID, value="NP5").get_attribute("value")
        self.butsud = driver.find_element(by=By.ID, value="NP6").get_attribute("value")
        self.mad = driver.find_element(by=By.ID, value="NP7").get_attribute("value")
        self.koudou = driver.find_element(by=By.ID, value="NP8").get_attribute("value")
        self.seimei = driver.find_element(by=By.ID, value="NP9").get_attribute("value")
        self.idou = driver.find_element(by=By.ID, value="ido").get_attribute("value")
        self.zenryokuidou = driver.find_element(by=By.ID, value="zenryoku_ido").get_attribute("value")
        self.money = driver.find_element(by=By.ID, value="money").get_attribute("value")
        self.reiryoku_dice_max = 10
        self.reimon_max = 22

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
        jsontext["data"]["status"][i]["label"] = "生命力"
        jsontext["data"]["status"][i]["value"] = int(self.seimei)
        jsontext["data"]["status"][i]["max"] = int(self.seimei)
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "霊紋"
        jsontext["data"]["status"][i]["value"] = int(self.reimon_max)
        jsontext["data"]["status"][i]["max"] = int(self.reimon_max)
        i = i + 1

        jsontext["data"]["params"] = []

        j = 0

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "体力"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.tairyoku)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "敏捷"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.binshou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知性"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.chisei)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "精神"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.seishin)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "幸運"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kouun)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "命中"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.meichu)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "回避"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kaihi)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "発動"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.hatsudou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "抵抗"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.teikou)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "看破"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.kanpa)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "物D"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.butsud)
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魔D"
        jsontext["data"]["params"][j]["value"] = none_to_str(self.mad)
        j = j + 1

        command = "//判定\n" + \
                  "2D6+{体力}+0 体力判定\n" + \
                  "2D6+{敏捷}+0 敏捷判定\n" + \
                  "2D6+{知性}+0 知性判定\n" + \
                  "2D6+{精神}+0 精神判定\n" + \
                  "2D6+{幸運}+0 幸運判定\n" + \
                  "2D6+{命中}+0 命中判定\n" + \
                  "2D6+{回避}+0 回避判定\n" + \
                  "2D6+{発動}+0 発動判定\n" + \
                  "2D6+{看破}+0 看破判定\n" + \
                  "\n//ダメージ\n" + \
                  "0+{物D}+0 物理ダメージ\n" + \
                  "0+{魔D}+0 魔法ダメージ\n" + \
                  "\n//生命力\n" + \
                  "C({生命力}-0) 残り生命力"

        jsontext["data"]["commands"] = command

        jsontext["data"]["externalUrl"] = self.url
        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_神我狩駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as filedata:  # 第二引数：writableオプションを指定
            json.dump(jsontext, filedata, ensure_ascii=False)

        print("神我狩駒データを生成しました")


def get_data(value):
    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    kamigakari = KamigakariData()
    time.sleep(5)

    kamigakari.input_data(driver, url)
    kamigakari.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"神我狩 ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1, text=u'キャラクターシートURL\nhttps://charasheet.vampire-blood.net/kmgkr_pc_making.html')
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