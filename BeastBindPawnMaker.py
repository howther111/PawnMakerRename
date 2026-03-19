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

class skills():
    name = ""
    type = ""
    level = 0
    timing = ""
    judge = ""
    target = ""
    range = ""
    cost = ""
    notes = ""


class items():
    name = ""
    type = ""
    timing = ""
    target = ""
    range = ""
    notes = ""


class weapons():
    name = ""
    type = ""
    judge = ""
    attribute = ""
    attack = ""
    guard = ""
    action = ""
    range = ""
    notes = ""

class OveredData():
    character_name = ""
    cord_name = ""
    player_name = ""
    style = ""
    primary_blood = ""
    secondary_blood = ""
    primary_root = ""
    secondary_root = ""

    body_base = 0
    skill_base = 0
    emotion_base = 0
    divine_base = 0
    society_base = 0
    body_bonus = 0
    skill_bonus = 0
    emotion_bonus = 0
    divine_bonus = 0
    society_bonus = 0
    body_armour = 0
    skill_armour = 0
    emotion_armour = 0
    divine_armour = 0
    society_armour = 0

    combat_base = 0
    shoot_base = 0
    dodge_base = 0
    action_base = 0
    combat_total = 0
    shoot_total = 0
    dodge_total = 0
    action_total = 0

    fp = 0
    humanity = 0
    bind_num = 0

    skills = []
    items = []
    weapons = []
    binds = []

    url = ""
    base_memo = ""

    def input_data(self, driver, input_url):
        self.url = input_url
        self.base_memo = driver.find_element(by=By.ID, value="base.memo").get_attribute("value")
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.cord_name = driver.find_element(by=By.ID, value="base.nameKana").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.style = driver.find_element(by=By.ID, value="base.style").get_attribute("value")
        self.primary_blood = driver.find_element(by=By.ID, value="base.bloods.primary.blood").get_attribute("value")
        self.secondary_blood = driver.find_element(by=By.ID, value="base.bloods.secondary.blood").get_attribute("value")
        self.primary_root = driver.find_element(by=By.ID, value="base.bloods.primary.root").get_attribute("value")
        self.secondary_root = driver.find_element(by=By.ID, value="base.bloods.secondary.root").get_attribute("value")
        self.body_base = driver.find_element(by=By.ID, value="baseAbility.body.total").get_attribute("value")
        self.skill_base = driver.find_element(by=By.ID, value="baseAbility.skill.total").get_attribute("value")
        self.emotion_base = driver.find_element(by=By.ID, value="baseAbility.emotion.total").get_attribute("value")
        self.divine_base = driver.find_element(by=By.ID, value="baseAbility.divine.total").get_attribute("value")
        self.society_base = driver.find_element(by=By.ID, value="baseAbility.society.total").get_attribute("value")
        self.body_bonus = driver.find_element(by=By.ID, value="baseAbility.body.tbonus").get_attribute("value")
        self.skill_bonus = driver.find_element(by=By.ID, value="baseAbility.skill.tbonus").get_attribute("value")
        self.emotion_bonus = driver.find_element(by=By.ID, value="baseAbility.emotion.tbonus").get_attribute("value")
        self.divine_bonus = driver.find_element(by=By.ID, value="baseAbility.divine.tbonus").get_attribute("value")
        self.society_bonus = driver.find_element(by=By.ID, value="baseAbility.society.tbonus").get_attribute("value")
        self.body_armour = driver.find_element(by=By.ID, value="baseAbility.body.tarmour").get_attribute("value")
        self.skill_armour = driver.find_element(by=By.ID, value="baseAbility.skill.tarmour").get_attribute("value")
        self.emotion_armour = driver.find_element(by=By.ID, value="baseAbility.emotion.tarmour").get_attribute("value")
        self.divine_armour = driver.find_element(by=By.ID, value="baseAbility.divine.tarmour").get_attribute("value")
        self.society_armour = driver.find_element(by=By.ID, value="baseAbility.society.tarmour").get_attribute("value")
        self.combat_base = driver.find_element(by=By.ID, value="battleAbility.combat.subtotal").get_attribute("value")
        self.shoot_base = driver.find_element(by=By.ID, value="battleAbility.shoot.subtotal").get_attribute("value")
        self.dodge_base = driver.find_element(by=By.ID, value="battleAbility.dodge.subtotal").get_attribute("value")
        self.action_base = driver.find_element(by=By.ID, value="battleAbility.action.subtotal").get_attribute("value")
        self.combat_total = driver.find_element(by=By.ID, value="battleAbility.combat.total").get_attribute("value")
        self.shoot_total = driver.find_element(by=By.ID, value="battleAbility.shoot.total").get_attribute("value")
        self.dodge_total = driver.find_element(by=By.ID, value="battleAbility.dodge.total").get_attribute("value")
        self.action_total = driver.find_element(by=By.ID, value="battleAbility.action.total").get_attribute("value")
        self.fp = driver.find_element(by=By.ID, value="fp.total").get_attribute("value")
        self.humanity = driver.find_element(by=By.ID, value="humanity.total").get_attribute("value")

        arts_0 = skills()
        arts_0.name = driver.find_element(by=By.ID, value="arts.0.name").get_attribute("value")
        arts_0.type = driver.find_element(by=By.ID, value="arts.0.type").get_attribute("value")
        arts_0.level = driver.find_element(by=By.ID, value="arts.0.level").get_attribute("value")
        arts_0.timing = driver.find_element(by=By.ID, value="arts.0.timing").get_attribute("value")
        arts_0.judge = driver.find_element(by=By.ID, value="arts.0.judge").get_attribute("value")
        arts_0.target = driver.find_element(by=By.ID, value="arts.0.target").get_attribute("value")
        arts_0.range = driver.find_element(by=By.ID, value="arts.0.range").get_attribute("value")
        arts_0.cost = driver.find_element(by=By.ID, value="arts.0.cost").get_attribute("value")
        arts_0.notes = driver.find_element(by=By.ID, value="arts.0.notes").get_attribute("value")
        if not arts_0.name == "":
            self.skills.append(arts_0)

        for i in range(98):
            try:
                artsnum = i + 1
                artstr = str(artsnum).zfill(3)
                arts = skills()

                artsnamestr = "arts." + artstr + ".name"
                artstypestr = "arts." + artstr + ".type"
                artslevelstr = "arts." + artstr + ".level"
                artstimingstr = "arts." + artstr + ".timing"
                artsjudgestr = "arts." + artstr + ".judge"
                artstargetstr = "arts." + artstr + ".target"
                artsrangestr = "arts." + artstr + ".range"
                artscoststr = "arts." + artstr + ".cost"
                artsnotesstr = "arts." + artstr + ".notes"
                arts.name = driver.find_element(by=By.ID, value=artsnamestr).get_attribute("value")
                arts.type = driver.find_element(by=By.ID, value=artstypestr).get_attribute("value")
                arts.level = driver.find_element(by=By.ID, value=artslevelstr).get_attribute("value")
                arts.timing = driver.find_element(by=By.ID, value=artstimingstr).get_attribute("value")
                arts.judge = driver.find_element(by=By.ID, value=artsjudgestr).get_attribute("value")
                arts.target = driver.find_element(by=By.ID, value=artstargetstr).get_attribute("value")
                arts.range = driver.find_element(by=By.ID, value=artsrangestr).get_attribute("value")
                arts.cost = driver.find_element(by=By.ID, value=artscoststr).get_attribute("value")
                arts.notes = driver.find_element(by=By.ID, value=artsnotesstr).get_attribute("value")
                self.skills.append(arts)
            except:
                break

        item_0 = items()
        item_0.name = driver.find_element(by=By.ID, value="items.0.name").get_attribute("value")
        item_0.type = driver.find_element(by=By.ID, value="items.0.type").get_attribute("value")
        item_0.timing = driver.find_element(by=By.ID, value="items.0.timing").get_attribute("value")
        item_0.target = driver.find_element(by=By.ID, value="items.0.target").get_attribute("value")
        item_0.range = driver.find_element(by=By.ID, value="items.0.range").get_attribute("value")
        item_0.notes = driver.find_element(by=By.ID, value="items.0.notes").get_attribute("value")
        if not item_0.name == "":
            self.items.append(item_0)

        for i in range(98):
            try:
                itemnum = i + 1
                itemstr = str(itemnum).zfill(3)
                item = items()

                itemnamestr = "items." + itemstr + ".name"
                itemtypestr = "items." + itemstr + ".type"
                itemtimingstr = "items." + itemstr + ".timing"
                itemtargetstr = "items." + itemstr + ".target"
                itemrangestr = "items." + itemstr + ".range"
                itemnotesstr = "items." + itemstr + ".notes"
                item.name = driver.find_element(by=By.ID, value=itemnamestr).get_attribute("value")
                item.type = driver.find_element(by=By.ID, value=itemtypestr).get_attribute("value")
                item.timing = driver.find_element(by=By.ID, value=itemtimingstr).get_attribute("value")
                item.judge = driver.find_element(by=By.ID, value=itemjudgestr).get_attribute("value")
                item.target = driver.find_element(by=By.ID, value=itemtargetstr).get_attribute("value")
                item.range = driver.find_element(by=By.ID, value=itemrangestr).get_attribute("value")
                item.notes = driver.find_element(by=By.ID, value=itemnotesstr).get_attribute("value")
                self.items.append(item)
            except:
                break

        bind_0 = driver.find_element(by=By.ID, value="binds.0.name").get_attribute("value")
        self.binds.append(bind_0)
        for i in range(98):
            try:
                bindnum = i + 1
                bindstr = str(bindnum).zfill(3)
                bind = ""

                bindnamestr = "binds." + bindstr + ".name"
                bind = driver.find_element(by=By.ID, value=bindnamestr).get_attribute("value")
                self.binds.append(bind)
            except:
                break

        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name + "\n" \
               "コードネーム:" + self.cord_name + "\n" \
               "PL:" + self.player_name + "\n"

        text = text + self.primary_blood
        if not self.secondary_blood == "":
            text = text + "/" + self.secondary_blood

        ##text = text + "\n" + self.primary_root
        ##if not self.secondary_root == "":
        ##    text = text + "/" + self.secondary_root

        if "<pawntext_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<pawntext_start>\n")[1]
            before_end = after_start.split("\n<pawntext_end>")[0]
            if "<no_default_pawntext>" in self.base_memo:
                text = before_end
            else:
                text = text + "\n\n" + before_end

        print(text)

        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_キャラクターテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("キャラクターテキストデータを生成しました")
        self.output_pawn(text)

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        self.action_total = self.action_total.replace("●", "")
        jsontext["data"]["initiative"] = int(self.action_total)
        jsontext["data"]["status"] = []

        i = 0
        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "FP"
        jsontext["data"]["status"][i]["value"] = self.fp
        jsontext["data"]["status"][i]["max"] = self.fp
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "人間性"
        jsontext["data"]["status"][i]["value"] = self.humanity
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        for j in self.binds:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = "絆/エゴ:" + j
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        for item in self.items:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = item.name
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        status_i = i

        jsontext["data"]["params"] = []
        k = 0

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "肉体"
        jsontext["data"]["params"][k]["value"] = self.body_armour
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "技術"
        jsontext["data"]["params"][k]["value"] = self.skill_armour
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "感情"
        jsontext["data"]["params"][k]["value"] = self.emotion_armour
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "加護"
        jsontext["data"]["params"][k]["value"] = self.divine_armour
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "社会"
        jsontext["data"]["params"][k]["value"] = self.society_armour
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "白兵値"
        jsontext["data"]["params"][k]["value"] = self.combat_total
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "射撃値"
        jsontext["data"]["params"][k]["value"] = self.shoot_total
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "回避値"
        jsontext["data"]["params"][k]["value"] = self.dodge_total
        k = k + 1

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = "//アクション\nムーブ:\nマイナー:\nメジャー:\n//リソース\n" + \
                                       "C({FP}-YY)　残りFP\n" + \
                                       "C({人間性}-YY)　残り人間性\n\n" + \
                                       "//能力値判定\n2BB+{肉体}+0  肉体判定\n" \
                                       "2BB+{技術}+0  技術判定\n" \
                                       "2BB+{感情}+0  感情判定\n" \
                                       "2BB+{加護}+0  加護判定\n" \
                                       "2BB+{社会}+0  社会判定\n" \
                                       "2BB+{白兵値}+0  白兵判定\n" \
                                       "2BB+{射撃値}+0  射撃判定\n" \
                                       "2BB+{回避値}+0  回避判定"

        """
        command = command + "\n//特技"
        for i in range(len(self.arts)):
            if not self.arts[i].name == "":
                command = command + "\n特技名:" + self.skill_name[i].replace("\n", "") + "/クラス:" + self.skill_class[i] + \
                          "/レベル:" + self.skill_level[i] + "/種別:" + self.skill_type[i] + "/タイミング:" + \
                          self.skill_timing[i] + "/対象:" + self.skill_target[i] + "/射程:" + self.skill_range[i] + \
                          "/代償:" +  self.skill_cost[i] + "/備考:" + self.skill_memo[i].replace("\n", "")

        command = command + "\n//加護"
        for i in range(len(self.specials)):
            if not self.specials[i] == "":
                command = command + "\n加護名:" + self.specials[i].replace("\n", "") + "/効果:" + self.specials_effect[i].replace("\n", "")

        command = command + "\n//アイテム"
        for i in range(len(self.items)):
            if not self.items[i] == "":
                command = command + "\nアイテム名:" + self.items[i].replace("\n", "") + "/効果:" + self.items_effect[i].replace("\n", "")
        """

        if "<chatpalette_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<chatpalette_start>\n")[1]
            before_end = after_start.split("\n<chatpalette_end>")[0]
            if "<no_default_chatpalette>" in self.base_memo:
                command = before_end
            else:
                command = command + "\n\n" + before_end

        i = status_i
        if "<status_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<status_start>\n")[1]
            before_end = after_start.split("\n<status_end>")[0]
            splitted_list = before_end.split("\n<status_splitter>\n")
            for splitted in splitted_list:
                label, value, max = splitted.split(",")
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = label
                jsontext["data"]["status"][i]["value"] = int(value)
                jsontext["data"]["status"][i]["max"] = int(max)
                i = i + 1

        j = k
        if "<params_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<params_start>\n")[1]
            before_end = after_start.split("\n<params_end>")[0]
            splitted_list = before_end.split("\n<params_splitter>\n")
            for splitted in splitted_list:
                label, value = splitted.split(",")
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][j]["label"] = label
                jsontext["data"]["params"][j]["value"] = value
                j = j + 1

        jsontext["data"]["commands"] = command
        jsontext["data"]["externalUrl"] = self.url
        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_キャラクター駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file, ensure_ascii=False)

        print("キャラクター駒データを生成しました")


def get_data(value):

    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    guardian = OveredData()
    time.sleep(5)

    guardian.input_data(driver, url)
    guardian.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"ビーストバインドトリニティ ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1,text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/bbt/')
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