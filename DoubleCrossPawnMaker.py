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

class skill():
    check = ""
    name = ""
    level = 0
    timing = ""
    type = ""
    judge = ""
    target = ""
    cost = ""
    limit = ""
    notes = ""


class items():
    name = ""
    skill = ""
    notes = ""


class OveredData():
    character_name = ""
    cord_name = ""
    player_name = ""
    syndrome_1 = ""
    syndrome_2 = ""
    syndrome_3 = ""

    body = 0
    sense = 0
    mind = 0
    society = 0

    hp = 0
    property_point = 0
    action = 0
    move_sen = 0
    move_zen = 0
    erotion = 0

    hak = 0
    sha = 0
    rc = 0
    kou = 0
    kai = 0
    tik = 0
    isi = 0
    tyo = 0
    skill_1 = []
    skill_2 = []
    skill_3 = []
    skill_4 = []
    skill_1_name = []
    skill_2_name = []
    skill_3_name = []
    skill_4_name = []
    lois_name = []
    memory_name = []
    combo = []
    arts = []
    items = []

    base_memo = ""

    url = ""

    def input_data(self, driver, input_url):

        self.base_memo = driver.find_element(by=By.ID, value="base.memo").get_attribute("value")
        self.url = input_url
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.cord_name = driver.find_element(by=By.ID, value="base.nameKana").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.syndrome_1 = driver.find_element(by=By.ID, value="base.syndromes.primary.syndrome").get_attribute("value")
        self.syndrome_2 = driver.find_element(by=By.ID, value="base.syndromes.secondary.syndrome").get_attribute("value")
        self.syndrome_3 = driver.find_element(by=By.ID, value="base.syndromes.tertiary.syndrome").get_attribute("value")
        self.body = driver.find_element(by=By.ID, value="baseAbility.body.total").get_attribute("value")
        self.sense = driver.find_element(by=By.ID, value="baseAbility.sense.total").get_attribute("value")
        self.mind = driver.find_element(by=By.ID, value="baseAbility.mind.total").get_attribute("value")
        self.society = driver.find_element(by=By.ID, value="baseAbility.society.total").get_attribute("value")

        self.hp = driver.find_element(by=By.ID, value="subAbility.hp.total").get_attribute("value")
        self.property_point = driver.find_element(by=By.ID, value="subAbility.property.total").get_attribute("value")
        self.action = driver.find_element(by=By.ID, value="subAbility.action.total").get_attribute("value")
        self.move_sen = driver.find_element(by=By.ID, value="subAbility.moveSen.total").get_attribute("value")
        self.move_zen = driver.find_element(by=By.ID, value="subAbility.moveZen.total").get_attribute("value")
        self.erotion = driver.find_element(by=By.ID, value="subAbility.erotion.total").get_attribute("value")

        self.hak = driver.find_element(by=By.ID, value="skills.hak.A.lv").get_attribute("value")
        self.sha = driver.find_element(by=By.ID, value="skills.sha.A.lv").get_attribute("value")
        self.rc = driver.find_element(by=By.ID, value="skills.rc.A.lv").get_attribute("value")
        self.kou = driver.find_element(by=By.ID, value="skills.kou.A.lv").get_attribute("value")
        self.kai = driver.find_element(by=By.ID, value="skills.kai.A.lv").get_attribute("value")
        self.tik = driver.find_element(by=By.ID, value="skills.tik.A.lv").get_attribute("value")
        self.isi = driver.find_element(by=By.ID, value="skills.isi.A.lv").get_attribute("value")
        self.tyo = driver.find_element(by=By.ID, value="skills.tyo.A.lv").get_attribute("value")
        self.skill_1.append(driver.find_element(by=By.ID, value="skills.B.0.lv1").get_attribute("value"))
        self.skill_2.append(driver.find_element(by=By.ID, value="skills.B.0.lv2").get_attribute("value"))
        self.skill_3.append(driver.find_element(by=By.ID, value="skills.B.0.lv3").get_attribute("value"))
        self.skill_4.append(driver.find_element(by=By.ID, value="skills.B.0.lv4").get_attribute("value"))
        self.skill_1_name.append(driver.find_element(by=By.ID, value="skills.B.0.name1").get_attribute("value"))
        self.skill_2_name.append(driver.find_element(by=By.ID, value="skills.B.0.name2").get_attribute("value"))
        self.skill_3_name.append(driver.find_element(by=By.ID, value="skills.B.0.name3").get_attribute("value"))
        self.skill_4_name.append(driver.find_element(by=By.ID, value="skills.B.0.name4").get_attribute("value"))

        for i in range(98):
            try:
                skillnum = i + 1
                skill1str = "skills.B." + str(skillnum).zfill(3) + ".lv1"
                skill2str = "skills.B." + str(skillnum).zfill(3) + ".lv2"
                skill3str = "skills.B." + str(skillnum).zfill(3) + ".lv3"
                skill4str = "skills.B." + str(skillnum).zfill(3) + ".lv4"
                self.skill_1.append(driver.find_element(by=By.ID, value=skill1str).get_attribute("value"))
                self.skill_2.append(driver.find_element(by=By.ID, value=skill2str).get_attribute("value"))
                self.skill_3.append(driver.find_element(by=By.ID, value=skill3str).get_attribute("value"))
                self.skill_4.append(driver.find_element(by=By.ID, value=skill4str).get_attribute("value"))
                skill1str = "skills.B." + str(skillnum).zfill(3) + ".name1"
                skill2str = "skills.B." + str(skillnum).zfill(3) + ".name2"
                skill3str = "skills.B." + str(skillnum).zfill(3) + ".name3"
                skill4str = "skills.B." + str(skillnum).zfill(3) + ".name4"
                self.skill_1_name.append(driver.find_element(by=By.ID, value=skill1str).get_attribute("value"))
                self.skill_2_name.append(driver.find_element(by=By.ID, value=skill2str).get_attribute("value"))
                self.skill_3_name.append(driver.find_element(by=By.ID, value=skill3str).get_attribute("value"))
                self.skill_4_name.append(driver.find_element(by=By.ID, value=skill4str).get_attribute("value"))
            except:
                break

        self.lois_name.append(driver.find_element(by=By.ID, value="lois.0.name").get_attribute("value"))
        for i in range(98):
            try:
                loisnum = i + 1
                loisstr = "lois." + str(loisnum).zfill(3) + ".name"
                self.lois_name.append(driver.find_element(by=By.ID, value=loisstr).get_attribute("value"))
            except:
                break

        self.memory_name.append(driver.find_element(by=By.ID, value="memory.0.name").get_attribute("value"))
        self.memory_name.append(driver.find_element(by=By.ID, value="memory.1.name").get_attribute("value"))
        self.memory_name.append(driver.find_element(by=By.ID, value="memory.2.name").get_attribute("value"))

        item_0 = items()
        item_0.name = driver.find_element(by=By.ID, value="items.0.name").get_attribute("value")
        item_0.skill = driver.find_element(by=By.ID, value="items.0.skill").get_attribute("value")
        item_0.notes = driver.find_element(by=By.ID, value="items.0.notes").get_attribute("value")
        if not item_0.name == "":
            self.items.append(item_0)

        for i in range(98):
            try:
                itemnum = i + 1
                itemstr = str(itemnum).zfill(3)
                item = items()

                itemnamestr = "items." + itemstr + ".name"
                itemskillstr = "items." + itemstr + ".skill"
                itemnotesstr = "items." + itemstr + ".notes"
                item.name = driver.find_element(by=By.ID, value=itemnamestr).get_attribute("value")
                item.skill = driver.find_element(by=By.ID, value=itemskillstr).get_attribute("value")
                item.notes = driver.find_element(by=By.ID, value=itemnotesstr).get_attribute("value")
                self.items.append(item)
            except:
                break

        skills_0 = skill()
        skills_0.check = driver.find_element(by=By.ID, value="arts.0.check").get_attribute("value")
        skills_0.name = driver.find_element(by=By.ID, value="arts.0.name").get_attribute("value")
        skills_0.level = int(driver.find_element(by=By.ID, value="arts.0.level").get_attribute("value"))
        skills_0.timing = driver.find_element(by=By.ID, value="arts.0.timing").get_attribute("value")
        skills_0.type = driver.find_element(by=By.ID, value="arts.0.type").get_attribute("value")
        skills_0.judge = driver.find_element(by=By.ID, value="arts.0.judge").get_attribute("value")
        skills_0.target = driver.find_element(by=By.ID, value="arts.0.target").get_attribute("value")
        skills_0.cost = driver.find_element(by=By.ID, value="arts.0.cost").get_attribute("value")
        skills_0.limit = driver.find_element(by=By.ID, value="arts.0.limit").get_attribute("value")
        skills_0.notes = driver.find_element(by=By.ID, value="arts.0.notes").get_attribute("value")
        self.arts.append(skills_0)

        for i in range(98):
            try:
                skillnum = i + 1
                skillstr = str(skillnum).zfill(3)
                skills = skill()

                skillcheckstr = "arts." + skillstr + ".check"
                skillnamestr = "arts." + skillstr + ".name"
                skilllevelstr = "arts." + skillstr + ".level"
                skilltimingstr = "arts." + skillstr + ".timing"
                skilltypestr = "arts." + skillstr + ".type"
                skilljudgestr = "arts." + skillstr + ".judge"
                skilltargetstr = "arts." + skillstr + ".target"
                skillcoststr = "arts." + skillstr + ".cost"
                skilllimitstr = "arts." + skillstr + ".limit"
                skillnotesstr = "arts." + skillstr + ".notes"

                skills.check = driver.find_element(by=By.ID, value=skillcheckstr).get_attribute("value")
                skills.skill = driver.find_element(by=By.ID, value=skillnamestr).get_attribute("value")
                skills.level = driver.find_element(by=By.ID, value=skilllevelstr).get_attribute("value")
                skills.timing = driver.find_element(by=By.ID, value=skilltimingstr).get_attribute("value")
                skills.type = driver.find_element(by=By.ID, value=skilltypestr).get_attribute("value")
                skills.judge = driver.find_element(by=By.ID, value=skilljudgestr).get_attribute("value")
                skills.target = driver.find_element(by=By.ID, value=skilltargetstr).get_attribute("value")
                skills.cost = driver.find_element(by=By.ID, value=skillcoststr).get_attribute("value")
                skills.limit = driver.find_element(by=By.ID, value=skilllimitstr).get_attribute("value")
                skills.notes = driver.find_element(by=By.ID, value=skillnotesstr).get_attribute("value")

                self.arts.append(skills)
            except:
                break

        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name + "\n" \
               "コードネーム:" + self.cord_name + "\n" \
               "PL:" + self.player_name + "\n"

        text = text + self.syndrome_1
        if not self.syndrome_2 == "":
            text = text + "/" + self.syndrome_2
        if not self.syndrome_3 == "":
            text = text + "/" + self.syndrome_3

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
        jsontext["data"]["initiative"] = int(self.action)
        jsontext["data"]["status"] = []

        i = 0
        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "HP"
        jsontext["data"]["status"][i]["value"] = self.hp
        jsontext["data"]["status"][i]["max"] = self.hp
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "侵蝕値"
        jsontext["data"]["status"][i]["value"] = self.erotion
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "侵蝕エフェクトLV修正"
        jsontext["data"]["status"][i]["value"] = 0
        jsontext["data"]["status"][i]["max"] = 3
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "侵蝕ダイス修正"
        jsontext["data"]["status"][i]["value"] = 0
        jsontext["data"]["status"][i]["max"] = 7
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "財産ポイント"
        jsontext["data"]["status"][i]["value"] = self.property_point
        jsontext["data"]["status"][i]["max"] = self.property_point
        i = i + 1

        for j in self.lois_name:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = "ロイス:" + j
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
        jsontext["data"]["params"][k]["label"] = "戦闘移動"
        jsontext["data"]["params"][k]["value"] = self.move_sen
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "全力移動"
        jsontext["data"]["params"][k]["value"] = self.move_zen
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "肉体"
        jsontext["data"]["params"][k]["value"] = self.body
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "感覚"
        jsontext["data"]["params"][k]["value"] = self.sense
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "精神"
        jsontext["data"]["params"][k]["value"] = self.mind
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "社会"
        jsontext["data"]["params"][k]["value"] = self.society
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "白兵"
        jsontext["data"]["params"][k]["value"] = self.hak
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "射撃"
        jsontext["data"]["params"][k]["value"] = self.sha
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "RC"
        jsontext["data"]["params"][k]["value"] = self.rc
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "交渉"
        jsontext["data"]["params"][k]["value"] = self.kou
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "回避"
        jsontext["data"]["params"][k]["value"] = self.kai
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "知覚"
        jsontext["data"]["params"][k]["value"] = self.tik
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "意志"
        jsontext["data"]["params"][k]["value"] = self.isi
        k = k + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][k]["label"] = "調達"
        jsontext["data"]["params"][k]["value"] = self.tyo
        k = k + 1

        for l in range(len(self.skill_1_name)):
            if not self.skill_1_name[l] == "":
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][k]["label"] = "運転:" + self.skill_1_name[l]
                jsontext["data"]["params"][k]["value"] = self.skill_1[l]
                k = k + 1

            if not self.skill_2_name[l] == "":
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][k]["label"] = "芸術:" + self.skill_2_name[l]
                jsontext["data"]["params"][k]["value"] = self.skill_2[l]
                k = k + 1

            if not self.skill_3_name[l] == "":
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][k]["label"] = "運転:" + self.skill_3_name[l]
                jsontext["data"]["params"][k]["value"] = self.skill_3[l]
                k = k + 1

            if not self.skill_4_name[l] == "":
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][k]["label"] = "芸術:" + self.skill_4_name[l]
                jsontext["data"]["params"][k]["value"] = self.skill_4[l]
                k = k + 1


        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = "//アクション\nマイナー:\nメジャー:\n//リソース\n" + \
                                       "C({HP}-YY)　残りHP\n\n" + \
                                       "//能力値判定\n({肉体}+{侵蝕ダイス修正})DX  肉体判定\n" \
                                       "({感覚}+{侵蝕ダイス修正}+0)DX  感覚判定\n" \
                                       "({精神}+{侵蝕ダイス修正}+0)DX  精神判定\n" \
                                       "({社会}+{侵蝕ダイス修正}+0)DX  社会判定\n"

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
    root.title(u"ダブルクロス3rd ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1,text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/dx3/')
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