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

class SkillData():
    name = ""
    skill_class = ""
    level = ""
    timing = ""
    target = ""
    range = ""
    cost = ""
    memo = ""

class HeroData():
    character_name = ""
    level = 0
    player_name = ""

    strong_total = 0
    strong_bonus = 0
    reflex_total = 0
    reflex_bonus = 0
    sense_total = 0
    sense_bonus = 0
    intellect_total = 0
    intellect_bonus = 0
    will_total = 0
    will_bonus = 0
    bllesing_total = 0
    bllesing_bonus = 0

    add_fortune_point = 0

    outfits_total_hit = 0
    outfits_total_dodge = 0
    outfits_total_magic = 0
    outfits_total_countermagic = 0
    outfits_total_action = 0
    outfits_total_hp = 0
    outfits_total_mp = 0
    outfits_total_kiai = 0
    outfits_total_attackHit = 0
    outfits_total_attackThrow = 0
    outfits_total_attackLock = 0
    outfits_total_battlespeed_total = ""

    armourstotal_hit = 0
    armourstotal_throw = 0
    armourstotal_lock = 0
    armourstotal_slash = 0
    armourstotal_bullet = 0

    items = []
    items_effect = []
    skills = []
    specials = []
    specials_1st = ""
    specials_2nd = ""
    specials_3rd = ""
    classes = []

    base_memo = ""

    break_flg = 0

    url = ""

    def input_data(self, driver, input_url):
        self.url = input_url
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.level = driver.find_element(by=By.ID, value="base.level").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.strong_total = driver.find_element(by=By.ID, value="abl.strong.total").get_attribute("value")
        self.strong_bonus = driver.find_element(by=By.ID, value="abl.strong.bonus").get_attribute("value")
        self.reflex_total = driver.find_element(by=By.ID, value="abl.reflex.total").get_attribute("value")
        self.reflex_bonus = driver.find_element(by=By.ID, value="abl.reflex.bonus").get_attribute("value")
        self.sense_total = driver.find_element(by=By.ID, value="abl.sense.total").get_attribute("value")
        self.sense_bonus = driver.find_element(by=By.ID, value="abl.sense.bonus").get_attribute("value")
        self.intellect_total = driver.find_element(by=By.ID, value="abl.intellect.total").get_attribute("value")
        self.intellect_bonus = driver.find_element(by=By.ID, value="abl.intellect.bonus").get_attribute("value")
        self.will_total = driver.find_element(by=By.ID, value="abl.will.total").get_attribute("value")
        self.will_bonus = driver.find_element(by=By.ID, value="abl.will.bonus").get_attribute("value")
        self.bllesing_total = driver.find_element(by=By.ID, value="abl.bllesing.total").get_attribute("value")
        self.bllesing_bonus = driver.find_element(by=By.ID, value="abl.bllesing.bonus").get_attribute("value")

        self.specials_1st = driver.find_element(by=By.ID, value="abl.specialpower.1st").get_attribute("value")
        self.specials_2nd = driver.find_element(by=By.ID, value="abl.specialpower.2nd").get_attribute("value")
        self.specials_3rd = driver.find_element(by=By.ID, value="abl.specialpower.3rd").get_attribute("value")

        first_special = SkillData()
        first_special.name = driver.find_element(by=By.ID, value="superskills.0.name").get_attribute("value")
        first_special.skill_class = driver.find_element(by=By.ID, value="superskills.0.class").get_attribute("value")
        first_special.level = driver.find_element(by=By.ID, value="superskills.0.level").get_attribute("value")
        first_special.timing = driver.find_element(by=By.ID, value="superskills.0.timing").get_attribute("value")
        first_special.target = driver.find_element(by=By.ID, value="superskills.0.target").get_attribute("value")
        first_special.range = driver.find_element(by=By.ID, value="superskills.0.range").get_attribute("value")
        first_special.cost = driver.find_element(by=By.ID, value="superskills.0.cost").get_attribute("value")
        first_special.memo = driver.find_element(by=By.ID, value="superskills.0.memo").get_attribute("value")

        self.base_memo = driver.find_element(by=By.ID, value="base.memo").get_attribute("value")

        self.specials.append(first_special)

        for i in range(98):
            try:
                specialnum = i + 1
                append_special = SkillData()

                namestr = "superskills." + str(specialnum).zfill(3) + ".name"
                append_special.name = driver.find_element(by=By.ID, value=namestr).get_attribute("value")

                skill_classstr = "superskills." + str(specialnum).zfill(3) + ".class"
                append_special.skill_class = driver.find_element(by=By.ID, value=skill_classstr).get_attribute(
                    "value")

                levelstr = "superskills." + str(specialnum).zfill(3) + ".level"
                append_special.level = driver.find_element(by=By.ID, value=levelstr).get_attribute("value")

                timingstr = "superskills." + str(specialnum).zfill(3) + ".timing"
                append_special.timing = driver.find_element(by=By.ID, value=timingstr).get_attribute(
                    "value")

                targetstr = "superskills." + str(specialnum).zfill(3) + ".target"
                append_special.target = driver.find_element(by=By.ID, value=targetstr).get_attribute(
                    "value")

                rangestr = "superskills." + str(specialnum).zfill(3) + ".range"
                append_special.range = driver.find_element(by=By.ID, value=rangestr).get_attribute("value")

                coststr = "superskills." + str(specialnum).zfill(3) + ".cost"
                append_special.cost = driver.find_element(by=By.ID, value=coststr).get_attribute("value")

                memostr = "superskills." + str(specialnum).zfill(3) + ".memo"
                append_special.memo = driver.find_element(by=By.ID, value=memostr).get_attribute("value")

                self.specials.append(append_special)
            except:
                break

        self.outfits_total_hit = driver.find_element(by=By.ID, value="outfits.total.hit").get_attribute("value")
        self.outfits_total_dodge = driver.find_element(by=By.ID, value="outfits.total.dodge").get_attribute("value")
        self.outfits_total_magic = driver.find_element(by=By.ID, value="outfits.total.magic").get_attribute("value")
        self.outfits_total_countermagic = driver.find_element(by=By.ID, value="outfits.total.countermagic").get_attribute("value")
        self.outfits_total_action = driver.find_element(by=By.ID, value="outfits.total.action").get_attribute("value")
        self.outfits_total_hp = driver.find_element(by=By.ID, value="outfits.total.hp").get_attribute("value")
        self.outfits_total_mp = driver.find_element(by=By.ID, value="outfits.total.mp").get_attribute("value")

        self.add_fortune_point = driver.find_element(by=By.ID, value="fortunepoint").get_attribute("value")

        self.outfits_total_attackHit = driver.find_element(by=By.ID, value="outfits.total.attackHit").get_attribute(
            "value")
        self.outfits_total_attackThrow = driver.find_element(by=By.ID, value="outfits.total.attackThrow").get_attribute(
            "value")
        self.outfits_total_attackLock = driver.find_element(by=By.ID, value="outfits.total.attackLock").get_attribute(
            "value")

        self.armourstotal_hit = driver.find_element(by=By.ID, value="armourstotal.hit").get_attribute("value")
        self.armourstotal_throw = driver.find_element(by=By.ID, value="armourstotal.throw").get_attribute("value")
        self.armourstotal_lock = driver.find_element(by=By.ID, value="armourstotal.lock").get_attribute("value")
        self.armourstotal_slash = driver.find_element(by=By.ID, value="armourstotal.slash").get_attribute("value")
        self.armourstotal_bullet = driver.find_element(by=By.ID, value="armourstotal.bullet").get_attribute("value")

        self.items.append(driver.find_element(by=By.ID, value="items.0.name").get_attribute("value"))

        for i in range(98):
            try:
                itemnum = i + 1
                itemstr = "items." + str(itemnum).zfill(3) + ".name"
                self.items.append(driver.find_element(by=By.ID, value=itemstr).get_attribute("value"))
            except:
                break

        self.items_effect.append(driver.find_element(by=By.ID, value="items.0.effect").get_attribute("value"))

        for i in range(98):
            try:
                itemnum = i + 1
                itemstr = "items." + str(itemnum).zfill(3) + ".effect"
                self.items_effect.append(driver.find_element(by=By.ID, value=itemstr).get_attribute("value"))
            except:
                break

        first_skill = SkillData()
        first_skill.name = driver.find_element(by=By.ID, value="skills.0.name").get_attribute("value")
        first_skill.skill_class = driver.find_element(by=By.ID, value="skills.0.class").get_attribute("value")
        first_skill.level = driver.find_element(by=By.ID, value="skills.0.level").get_attribute("value")
        first_skill.timing = driver.find_element(by=By.ID, value="skills.0.timing").get_attribute("value")
        first_skill.target = driver.find_element(by=By.ID, value="skills.0.timing").get_attribute("value")
        first_skill.range = driver.find_element(by=By.ID, value="skills.0.timing").get_attribute("value")
        first_skill.cost = driver.find_element(by=By.ID, value="skills.0.timing").get_attribute("value")
        first_skill.memo = driver.find_element(by=By.ID, value="skills.0.timing").get_attribute("value")

        self.skills.append(first_skill)

        for i in range(98):
            try:
                skillnum = i + 1
                append_skill = SkillData()

                namestr = "skills." + str(skillnum).zfill(3) + ".name"
                append_skill.name = driver.find_element(by=By.ID, value=namestr).get_attribute("value")

                skill_classstr = "skills." + str(skillnum).zfill(3) + ".class"
                append_skill.skill_class = driver.find_element(by=By.ID, value=skill_classstr).get_attribute(
                    "value")

                levelstr = "skills." + str(skillnum).zfill(3) + ".level"
                append_skill.level = driver.find_element(by=By.ID, value="skills.levelstr.level").get_attribute("value")

                timingstr = "skills." + str(skillnum).zfill(3) + ".timing"
                append_skill.timing = driver.find_element(by=By.ID, value="skills.timingstr.timing").get_attribute(
                    "value")

                targetstr = "skills." + str(skillnum).zfill(3) + ".target"
                append_skill.target = driver.find_element(by=By.ID, value=targetstr).get_attribute(
                    "value")

                rangestr = "skills." + str(skillnum).zfill(3) + ".range"
                append_skill.range = driver.find_element(by=By.ID, value=rangestr).get_attribute("value")

                coststr = "skills." + str(skillnum).zfill(3) + ".cost"
                append_skill.cost = driver.find_element(by=By.ID, value=coststr).get_attribute("value")

                memostr = "skills." + str(skillnum).zfill(3) + ".memo"
                append_skill.memo = driver.find_element(by=By.ID, value=memostr).get_attribute("value")

                self.skills.append(append_skill)
            except:
                break

        first_class = driver.find_element(by=By.ID, value="classes.0.name").get_attribute("value")
        self.classes.append(first_class)

        for i in range(98):
            try:
                classnum = i + 1
                append_classstr = "classes." + str(classnum).zfill(3) + ".name"
                append_class = driver.find_element(by=By.ID, value=append_classstr).get_attribute("value")
                self.classes.append(append_class)
            except:
                break

        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name +  \
                   "\nPL:" + self.player_name + " レベル:" + self.level

        text = text + "\n財産ポイント:" + self.add_fortune_point

        text = text + "\n【命中】" + str(self.outfits_total_hit) + \
                   "【回避】" + str(self.outfits_total_dodge) + \
                   "【組手】" + str(self.outfits_total_magic) + \
                   "【受身】" + str(self.outfits_total_countermagic) + \
                   "【行動】" + str(self.outfits_total_action) + \
                   "\n" + \
                   "【耐久】" + str(self.outfits_total_hp) + \
                   "【精神】" + str(self.outfits_total_mp) + \
                   "\n【殴攻撃力】" + str(self.outfits_total_attackHit) + \
                   "【投攻撃力】" + str(self.outfits_total_attackThrow) + \
                   "【極攻撃力】" + str(self.outfits_total_attackLock)

        text = text + "\nクラス:"
        for plus_class in self.classes:
            text = text + plus_class + "/"
        text = text[:-1]

        text = text + "\n奥義:"
        text = text + self.specials_1st + "/" + self.specials_2nd + "/" + self.specials_3rd

        text = text + "\nアイテム:"
        for item in self.items:
            text = text + item + "/"
        text = text[:-1]

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
        self.output_porn(text)

    def output_porn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.outfits_total_action)
        jsontext["data"]["status"] = []

        i = 0

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "HP"
        jsontext["data"]["status"][i]["value"] = self.outfits_total_hp
        jsontext["data"]["status"][i]["max"] = self.outfits_total_hp
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "MP"
        jsontext["data"]["status"][i]["value"] = self.outfits_total_mp
        jsontext["data"]["status"][i]["max"] = self.outfits_total_mp
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "気合カード"
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 99
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "財産ポイント"
        jsontext["data"]["status"][i]["value"] = self.add_fortune_point
        jsontext["data"]["status"][i]["max"] = self.add_fortune_point
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "奈落落ち"
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = self.specials_1st
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = self.specials_2nd
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = self.specials_3rd
        jsontext["data"]["status"][i]["value"] = 1
        jsontext["data"]["status"][i]["max"] = 1
        i = i + 1

        for item in self.items:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = item
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        status_i = i

        jsontext["data"]["params"] = []

        j = 0

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "レベル"
        jsontext["data"]["params"][j]["value"] = self.level
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "体力基本値"
        jsontext["data"]["params"][j]["value"] = self.strong_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "反射基本値"
        jsontext["data"]["params"][j]["value"] = self.reflex_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知覚基本値"
        jsontext["data"]["params"][j]["value"] = self.sense_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "理知基本値"
        jsontext["data"]["params"][j]["value"] = self.intellect_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "意志基本値"
        jsontext["data"]["params"][j]["value"] = self.will_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "幸運基本値"
        jsontext["data"]["params"][j]["value"] = self.bllesing_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "体力B"
        jsontext["data"]["params"][j]["value"] = self.strong_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "反射B"
        jsontext["data"]["params"][j]["value"] = self.reflex_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知覚B"
        jsontext["data"]["params"][j]["value"] = self.sense_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "理知B"
        jsontext["data"]["params"][j]["value"] = self.intellect_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "意志B"
        jsontext["data"]["params"][j]["value"] = self.will_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "幸運B"
        jsontext["data"]["params"][j]["value"] = self.bllesing_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "命中値"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_hit
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "回避値"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_dodge
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "組手値"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_magic
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "受身値"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_countermagic
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "行動値"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_action
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "殴攻撃力"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_attackHit
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "投攻撃力"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_attackThrow
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "極攻撃力"
        jsontext["data"]["params"][j]["value"] = self.outfits_total_attackLock
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "投防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_throw
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "極防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_lock
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "殴防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_hit
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "投防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_throw
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "極防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_lock
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "斬防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_slash
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "弾防御"
        jsontext["data"]["params"][j]["value"] = self.armourstotal_bullet
        j = j + 1

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = "//アクション\nムーブ:\nマイナー:\nメジャー:\n//リソース\n" + \
                                       "C({HP}-YY)　残りHP\n" + \
                                       "C({MP}-YY)　残りMP\n\n" + \
                                       "//防御、+0欄に修正を記入\n2d6+{回避値}+0　回避\n" \
                                       "2d6+{受身値}+0　受身\nC(XX-{}-0)　被ダメージ、{}内に防御属性3文字\n\n" \
                                       "//攻撃、+0欄に修正を記入\n2d6+{命中値}+0　命中\n2d6+{組手値}+0　組手\n" + \
                                       "2d6+{殴攻撃力}+0　" + \
                                       "〈殴〉ダメージ\n" \
                                       "2d6+{投攻撃力}+0　" + \
                                       "〈投〉ダメージ\n" \
                                       "2d6+{極攻撃力}+0　" + \
                                       "〈極〉ダメージ\n" \
                  "\n//能力値判定\n2d6+{体力B}  体力判定\n2d6+{反射B}  反射判定\n2d6+{知覚B}  " \
                                       "知覚判定\n2d6+{理知B}  理知判定\n2d6+{意志B}  意志判定\n2d6+{幸運B}  幸運判定"
        command = command + "\n//奥義"
        for skill in self.specials:
            if not skill.name == "":
                command = command + "\n奥義名:" + skill.name.replace("\n", "") + "/クラス:" + skill.skill_class + \
                          "/レベル:" + skill.level + "/タイミング:" + \
                          skill.timing + "/対象:" + skill.target + "/射程:" + skill.range + \
                          "/代償:" + skill.cost + "/備考:" + skill.memo.replace("\n", "")

        command = command + "\n//特技"
        for skill in self.skills:
            if not skill.name == "":
                command = command + "\n特技名:" + skill.name.replace("\n", "") + "/クラス:" + skill.skill_class + \
                          "/レベル:" + skill.level + "/タイミング:" + \
                          skill.timing + "/対象:" + skill.target + "/射程:" + skill.range + \
                          "/代償:" + skill.cost + "/備考:" + skill.memo.replace("\n", "")

        command = command + "\n//アイテム"
        for i in range(len(self.items)):
            if not self.items[i] == "":
                command = command + "\nアイテム名:" + self.items[i].replace("\n", "") + "/効果:" + self.items_effect[i].replace("\n", "")

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
    guardian = HeroData()
    time.sleep(5)

    guardian.input_data(driver, url)
    guardian.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"拳禅無双RPG ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1,text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/kenzen/')
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