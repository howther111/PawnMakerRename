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


class GuardianData():
    base_memo = ""
    character_name = ""
    guardian_name = ""
    level = 0
    guardian_size = ""
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
    outfits_total_fp = 0
    outfits_total_hp = 0
    outfits_total_mp = 0
    outfits_total_attack = 0
    outfits_total_battlespeed_total = ""

    outfits_main_weapon_shortname = ""
    outfits_main_weapon_shortattack = ""
    outfits_main_weapon_shortrange = ""
    outfits_main_weapon_shortstrong = ""

    outfits_sub_weapon_shortname = ""
    outfits_sub_weapon_shortattack = ""
    outfits_sub_weapon_shortrange = ""
    outfits_sub_weapon_shortstrong = ""

    outfits_main_weapon_longname = ""
    outfits_main_weapon_longattack = ""
    outfits_main_weapon_longrange = ""
    outfits_main_weapon_longstrong = ""

    outfits_sub_weapon_longname = ""
    outfits_sub_weapon_longattack = ""
    outfits_sub_weapon_longrange = ""
    outfits_sub_weapon_longstrong = ""

    armourstotal_slash = 0
    armourstotal_pierce = 0
    armourstotal_crash = 0
    armourstotal_fire = 0
    armourstotal_ice = 0
    armourstotal_thunder = 0
    armourstotal_light = 0
    armourstotal_dark = 0

    items = []
    specials = []
    items_effect = []
    specials_effect = []
    skill_name = []
    skill_class = []
    skill_level = []
    skill_type = []
    skill_timing = []
    skill_target = []
    skill_range = []
    skill_cost = []
    skill_memo = []
    class_name = []
    class_level = []

    break_flg = 0

    url = ""

    def input_data(self, driver, input_url):
        self.url = input_url
        self.base_memo = driver.find_element(by=By.ID, value="base.memo").get_attribute("value")
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.guardian_name = driver.find_element(by=By.ID, value="base.guardian.name").get_attribute("value")
        self.level = driver.find_element(by=By.ID, value="base.level").get_attribute("value")
        self.guardian_size = driver.find_element(by=By.ID, value="base.guardian.size").get_attribute("value")
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

        self.specials.append(driver.find_element(by=By.ID, value="specials.0.name").get_attribute("value"))

        for i in range(98):
            try:
                specialnum = i + 1
                specialstr = "specials." + str(specialnum).zfill(3) + ".name"
                self.specials.append(driver.find_element(by=By.ID, value=specialstr).get_attribute("value"))
            except:
                break

        self.specials_effect.append(driver.find_element(by=By.ID, value="specials.0.effect").get_attribute("value"))

        for i in range(98):
            try:
                specialnum = i + 1
                specialstr = "specials." + str(specialnum).zfill(3) + ".effect"
                self.specials_effect.append(driver.find_element(by=By.ID, value=specialstr).get_attribute("value"))
            except:
                break

        self.outfits_total_hit = driver.find_element(by=By.ID, value="outfits.total.hit").get_attribute("value")
        self.outfits_total_dodge = driver.find_element(by=By.ID, value="outfits.total.dodge").get_attribute("value")
        self.outfits_total_magic = driver.find_element(by=By.ID, value="outfits.total.magic").get_attribute("value")
        self.outfits_total_countermagic = driver.find_element(by=By.ID, value="outfits.total.countermagic").get_attribute("value")
        self.outfits_total_action = driver.find_element(by=By.ID, value="outfits.total.action").get_attribute("value")
        self.outfits_total_fp = driver.find_element(by=By.ID, value="outfits.total.fp").get_attribute("value")
        self.outfits_total_hp = driver.find_element(by=By.ID, value="outfits.total.hp").get_attribute("value")
        self.outfits_total_mp = driver.find_element(by=By.ID, value="outfits.total.mp").get_attribute("value")
        self.outfits_total_action = driver.find_element(by=By.ID, value="outfits.total.action").get_attribute("value")
        self.outfits_total_battlespeed_total = driver.find_element(by=By.ID, value="outfits.total.battlespeed.total").get_attribute("value")
        self.outfits_total_battlespeed_total = self.outfits_total_battlespeed_total.replace("ﾏｽ", "")

        self.add_fortune_point = driver.find_element(by=By.ID, value="addfortunepoint").get_attribute("value")

        self.outfits_main_weapon_shortname = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortname").get_attribute("value")
        self.outfits_main_weapon_shortattack = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortattack").get_attribute("value")
        self.outfits_main_weapon_shortrange = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortrange").get_attribute("value")
        self.outfits_main_weapon_shortstrong = driver.find_element(by=By.ID, value="outfits.total.main_weapon_shortstrong").get_attribute("value")

        self.outfits_sub_weapon_shortname = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortname").get_attribute("value")
        self.outfits_sub_weapon_shortattack = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortattack").get_attribute("value")
        self.outfits_sub_weapon_shortrange = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortrange").get_attribute("value")
        self.outfits_sub_weapon_shortstrong = driver.find_element(by=By.ID, value="outfits.total.sub_weapon_shortstrong").get_attribute("value")

        self.outfits_main_weapon_longname = driver.find_element(by=By.ID,
                                                                value="outfits.total.main_weapon_longname").get_attribute(
            "value")
        self.outfits_main_weapon_longattack = driver.find_element(by=By.ID,
                                                                  value="outfits.total.main_weapon_longattack").get_attribute(
            "value")
        self.outfits_main_weapon_longrange = driver.find_element(by=By.ID,
                                                                 value="outfits.total.main_weapon_longrange").get_attribute(
            "value")
        self.outfits_main_weapon_longstrong = driver.find_element(by=By.ID,
                                                                  value="outfits.total.main_weapon_longstrong").get_attribute(
            "value")

        self.outfits_sub_weapon_longname = driver.find_element(by=By.ID,
                                                               value="outfits.total.sub_weapon_longname").get_attribute(
            "value")
        self.outfits_sub_weapon_longattack = driver.find_element(by=By.ID,
                                                                 value="outfits.total.sub_weapon_longattack").get_attribute(
            "value")
        self.outfits_sub_weapon_longrange = driver.find_element(by=By.ID,
                                                                value="outfits.total.sub_weapon_longrange").get_attribute(
            "value")
        self.outfits_sub_weapon_longstrong = driver.find_element(by=By.ID,
                                                                 value="outfits.total.sub_weapon_longstrong").get_attribute(
            "value")

        self.armourstotal_slash = driver.find_element(by=By.ID, value="armourstotal.slash").get_attribute("value")
        self.armourstotal_pierce = driver.find_element(by=By.ID, value="armourstotal.pierce").get_attribute("value")
        self.armourstotal_crash = driver.find_element(by=By.ID, value="armourstotal.crash").get_attribute("value")
        self.armourstotal_fire = driver.find_element(by=By.ID, value="armourstotal.fire").get_attribute("value")
        self.armourstotal_ice = driver.find_element(by=By.ID, value="armourstotal.ice").get_attribute("value")
        self.armourstotal_thunder = driver.find_element(by=By.ID, value="armourstotal.thunder").get_attribute("value")
        self.armourstotal_light = driver.find_element(by=By.ID, value="armourstotal.light").get_attribute("value")
        self.armourstotal_dark = driver.find_element(by=By.ID, value="armourstotal.dark").get_attribute("value")

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

        skillnamestr = "skills.0.name"
        self.skill_name.append(driver.find_element(by=By.ID, value=skillnamestr).get_attribute("value"))

        skillclassstr = "skills.0.class"
        self.skill_class.append(driver.find_element(by=By.ID, value=skillclassstr).get_attribute("value"))

        skilllevelstr = "skills.0.level"
        self.skill_level.append(driver.find_element(by=By.ID, value=skilllevelstr).get_attribute("value"))

        skilltypestr = "skills.0.type"
        self.skill_type.append(driver.find_element(by=By.ID, value=skilltypestr).get_attribute("value"))

        skilltimingstr = "skills.0.timing"
        self.skill_timing.append(driver.find_element(by=By.ID, value=skilltimingstr).get_attribute("value"))

        skilltargetstr = "skills.0.target"
        self.skill_target.append(driver.find_element(by=By.ID, value=skilltargetstr).get_attribute("value"))

        skillrangestr = "skills.0.range"
        self.skill_range.append(driver.find_element(by=By.ID, value=skillrangestr).get_attribute("value"))

        skillcoststr = "skills.0.cost"
        self.skill_cost.append(driver.find_element(by=By.ID, value=skillcoststr).get_attribute("value"))

        skillmemostr = "skills.0.memo"
        self.skill_memo.append(driver.find_element(by=By.ID, value=skillmemostr).get_attribute("value"))

        for i in range(998):
            try:
                skillnum = i + 1
                skillnamestr = "skills." + str(skillnum).zfill(3) + ".name"
                self.skill_name.append(driver.find_element(by=By.ID, value=skillnamestr).get_attribute("value"))

                skillclassstr = "skills." + str(skillnum).zfill(3) + ".class"
                self.skill_class.append(driver.find_element(by=By.ID, value=skillclassstr).get_attribute("value"))

                skilllevelstr = "skills." + str(skillnum).zfill(3) + ".level"
                self.skill_level.append(driver.find_element(by=By.ID, value=skilllevelstr).get_attribute("value"))

                skilltypestr = "skills." + str(skillnum).zfill(3) + ".type"
                self.skill_type.append(driver.find_element(by=By.ID, value=skilltypestr).get_attribute("value"))

                skilltimingstr = "skills." + str(skillnum).zfill(3) + ".timing"
                self.skill_timing.append(driver.find_element(by=By.ID, value=skilltimingstr).get_attribute("value"))

                skilltargetstr = "skills." + str(skillnum).zfill(3) + ".target"
                self.skill_target.append(driver.find_element(by=By.ID, value=skilltargetstr).get_attribute("value"))

                skillrangestr = "skills." + str(skillnum).zfill(3) + ".range"
                self.skill_range.append(driver.find_element(by=By.ID, value=skillrangestr).get_attribute("value"))

                skillcoststr = "skills." + str(skillnum).zfill(3) + ".cost"
                self.skill_cost.append(driver.find_element(by=By.ID, value=skillcoststr).get_attribute("value"))

                skillmemostr = "skills." + str(skillnum).zfill(3) + ".memo"
                self.skill_memo.append(driver.find_element(by=By.ID, value=skillmemostr).get_attribute("value"))
            except:
                break

        classnamestr = "classes.0.name"
        classlevelstr = "classes.0.level"
        self.class_name.append(driver.find_element(by=By.ID, value=classnamestr).get_attribute("value"))
        self.class_level.append(driver.find_element(by=By.ID, value=classlevelstr).get_attribute("value"))
        if self.class_name[0] == "":
            classnamestr2 = "classes.0.nametext"
            self.class_name[0] = driver.find_element(by=By.ID, value=classnamestr2).get_attribute("value")

        for i in range(98):
            try:
                classnum = i + 1
                classnamestr = "classes." + str(classnum).zfill(3) + ".name"
                classlevelstr = "classes." + str(classnum).zfill(3) + ".level"
                self.class_name.append(driver.find_element(by=By.ID, value=classnamestr).get_attribute("value"))
                self.class_level.append(driver.find_element(by=By.ID, value=classlevelstr).get_attribute("value"))
                if self.class_name[classnum] == "":
                    classnamestr2 = "classes." + str(classnum).zfill(3) + ".nametext"
                    self.class_name[classnum] = driver.find_element(by=By.ID, value=classnamestr2).get_attribute("value")
            except:
                break

        print(self.guardian_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "ガーディアン:" + self.guardian_name + "\n" + \
                   "PC:" + self.character_name +  \
                   " PL:" + self.player_name + "\n" + \
                   "レベル:" + self.level + \
                   " サイズ:" + self.guardian_size

        text = text + "\n財産ポイント:" + self.add_fortune_point

        text = text + "\n【命中】" + str(self.outfits_total_hit) + \
                   "【回避】" + str(self.outfits_total_dodge) + \
                   "【砲撃】" + str(self.outfits_total_magic) + \
                   "【防壁】" + str(self.outfits_total_countermagic) + \
                   "【行動】" + str(self.outfits_total_action) + \
                   "\n【力場】" + str(self.outfits_total_fp) + \
                   "【耐久】" + str(self.outfits_total_hp) + \
                   "【感応】" + str(self.outfits_total_mp) + \
                   "【移動力】" + str(self.outfits_total_battlespeed_total)

        text = text + "\n加護:"
        for special in self.specials:
            text = text + special + "/"
        text = text[:-1]

        text = text + "\n[*]主近:" + self.outfits_main_weapon_shortname + \
                " 射程:" + self.outfits_main_weapon_shortrange + \
                " 代償:" + self.outfits_main_weapon_shortstrong + \
                "\n攻撃力:" + self.outfits_main_weapon_shortattack

        text = text + "\n[*]副近:" + self.outfits_sub_weapon_shortname + \
                " 射程:" + self.outfits_sub_weapon_shortrange + \
                " 代償:" + self.outfits_sub_weapon_shortstrong + \
                "\n攻撃力:" + self.outfits_sub_weapon_shortattack

        text = text + "\n[*]主遠:" + self.outfits_main_weapon_longname + \
                   " 射程:" + self.outfits_main_weapon_longrange + \
                   " 代償:" + self.outfits_main_weapon_longstrong + \
                   "\n攻撃力:" + self.outfits_main_weapon_longattack

        text = text + "\n[*]副遠:" + self.outfits_sub_weapon_longname + \
                   " 射程:" + self.outfits_sub_weapon_longrange + \
                   " 代償:" + self.outfits_sub_weapon_longstrong + \
                   "\n攻撃力:" + self.outfits_sub_weapon_longattack

        text = text + "\n防御力:斬" + self.armourstotal_slash + \
                "/刺" + self.armourstotal_pierce + \
                "/殴" + self.armourstotal_crash + \
                "/炎" + self.armourstotal_fire + \
                "/氷" + self.armourstotal_ice + \
                "/雷" + self.armourstotal_thunder + \
                "/光" + self.armourstotal_light + \
                "/闇" + self.armourstotal_dark

        #text = text + "\nアイテム:"
        #for item in self.items:
        #    text = text + item + "/"
        #text = text[:-1]

        if "<pawntext_guardian_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<pawntext_guardian_start>\n")[1]
            before_end = after_start.split("\n<pawntext_guardian_end>")[0]
            if "<no_default_guardian_pawntext>" in self.base_memo:
                text = before_end
            else:
                text = text + "\n\n" + before_end

        print(text)

        file_name = self.guardian_name.replace("/", "_").replace("\"", "”") + "_ガーディアンテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("ガーディアンテキストデータを生成しました")
        self.output_pawn(text)

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.guardian_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.outfits_total_action)
        jsontext["data"]["status"] = []

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][0]["label"] = "FP"
        jsontext["data"]["status"][0]["value"] = self.outfits_total_fp
        jsontext["data"]["status"][0]["max"] = self.outfits_total_fp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][1]["label"] = "HP"
        jsontext["data"]["status"][1]["value"] = self.outfits_total_hp
        jsontext["data"]["status"][1]["max"] = self.outfits_total_hp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][2]["label"] = "EN"
        jsontext["data"]["status"][2]["value"] = self.outfits_total_mp
        jsontext["data"]["status"][2]["max"] = self.outfits_total_mp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][3]["label"] = "財産ポイント"
        jsontext["data"]["status"][3]["value"] = self.add_fortune_point
        jsontext["data"]["status"][3]["max"] = self.add_fortune_point

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][4]["label"] = "ブレイク"
        jsontext["data"]["status"][4]["value"] = 1
        jsontext["data"]["status"][4]["max"] = 1

        i = 5

        for special in self.specials:
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = special
            jsontext["data"]["status"][i]["value"] = 1
            jsontext["data"]["status"][i]["max"] = 1
            i = i + 1

        for item in self.items:
            itemnum = item.split("*")
            if len(itemnum) > 1:
                if not ("非表示" in item or "非消費" in item):
                    jsontext["data"]["status"].append({})
                    jsontext["data"]["status"][i]["label"] = itemnum[0]
                    jsontext["data"]["status"][i]["value"] = itemnum[1]
                    jsontext["data"]["status"][i]["max"] = itemnum[1]
                    i = i + 1
            else:
                if not ("非表示" in item or "非消費" in item):
                    jsontext["data"]["status"].append({})
                    jsontext["data"]["status"][i]["label"] = item
                    jsontext["data"]["status"][i]["value"] = 1
                    jsontext["data"]["status"][i]["max"] = 1
                    i = i + 1

        if "/" in self.outfits_main_weapon_shortstrong:
            mws_ammo = self.outfits_main_weapon_shortstrong.split("/")
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = self.outfits_main_weapon_shortname + "弾数"
            jsontext["data"]["status"][i]["value"] = mws_ammo[1]
            jsontext["data"]["status"][i]["max"] = mws_ammo[1]
            i = i + 1

        if "/" in self.outfits_sub_weapon_shortstrong:
            sws_ammo = self.outfits_sub_weapon_shortstrong.split("/")
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = self.outfits_sub_weapon_shortname + "弾数"
            jsontext["data"]["status"][i]["value"] = sws_ammo[1]
            jsontext["data"]["status"][i]["max"] = sws_ammo[1]
            i = i + 1

        if "/" in self.outfits_main_weapon_longstrong:
            mwl_ammo = self.outfits_main_weapon_longstrong.split("/")
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = self.outfits_main_weapon_longname + "弾数"
            jsontext["data"]["status"][i]["value"] = mwl_ammo[1]
            jsontext["data"]["status"][i]["max"] = mwl_ammo[1]
            i = i + 1

        if "/" in self.outfits_sub_weapon_longstrong:
            swl_ammo = self.outfits_sub_weapon_longstrong.split("/")
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = self.outfits_sub_weapon_longname + "弾数"
            jsontext["data"]["status"][i]["value"] = swl_ammo[1]
            jsontext["data"]["status"][i]["max"] = swl_ammo[1]
            i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "クリティカル値"
        jsontext["data"]["status"][i]["value"] = 12
        jsontext["data"]["status"][i]["max"] = 13
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "ファンブル値"
        jsontext["data"]["status"][i]["value"] = 2
        jsontext["data"]["status"][i]["max"] = 13
        i = i + 1
        status_i = i

        jsontext["data"]["params"] = []

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][0]["label"] = "体力基本値"
        jsontext["data"]["params"][0]["value"] = self.strong_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][1]["label"] = "反射基本値"
        jsontext["data"]["params"][1]["value"] = self.sense_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][2]["label"] = "知覚基本値"
        jsontext["data"]["params"][2]["value"] = self.strong_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][3]["label"] = "理知基本値"
        jsontext["data"]["params"][3]["value"] = self.intellect_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][4]["label"] = "意志基本値"
        jsontext["data"]["params"][4]["value"] = self.will_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][5]["label"] = "幸運基本値"
        jsontext["data"]["params"][5]["value"] = self.bllesing_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][6]["label"] = "体力B"
        jsontext["data"]["params"][6]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][7]["label"] = "反射B"
        jsontext["data"]["params"][7]["value"] = self.sense_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][8]["label"] = "知覚B"
        jsontext["data"]["params"][8]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][9]["label"] = "理知B"
        jsontext["data"]["params"][9]["value"] = self.intellect_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][10]["label"] = "意志B"
        jsontext["data"]["params"][10]["value"] = self.will_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][11]["label"] = "幸運B"
        jsontext["data"]["params"][11]["value"] = self.bllesing_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][12]["label"] = "命中値"
        jsontext["data"]["params"][12]["value"] = self.outfits_total_hit

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][13]["label"] = "回避値"
        jsontext["data"]["params"][13]["value"] = self.outfits_total_dodge

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][14]["label"] = "砲撃値"
        jsontext["data"]["params"][14]["value"] = self.outfits_total_magic

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][15]["label"] = "防壁値"
        jsontext["data"]["params"][15]["value"] = self.outfits_total_countermagic

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][16]["label"] = "行動値"
        jsontext["data"]["params"][16]["value"] = self.outfits_total_action

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][17]["label"] = "移動力"
        jsontext["data"]["params"][17]["value"] = self.outfits_total_battlespeed_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][18]["label"] = "斬防御"
        jsontext["data"]["params"][18]["value"] = self.armourstotal_slash

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][19]["label"] = "刺防御"
        jsontext["data"]["params"][19]["value"] = self.armourstotal_pierce

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][20]["label"] = "殴防御"
        jsontext["data"]["params"][20]["value"] = self.armourstotal_crash

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][21]["label"] = "炎防御"
        jsontext["data"]["params"][21]["value"] = self.armourstotal_fire

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][22]["label"] = "氷防御"
        jsontext["data"]["params"][22]["value"] = self.armourstotal_ice

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][23]["label"] = "雷防御"
        jsontext["data"]["params"][23]["value"] = self.armourstotal_thunder

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][24]["label"] = "光防御"
        jsontext["data"]["params"][24]["value"] = self.armourstotal_light

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][25]["label"] = "闇防御"
        jsontext["data"]["params"][25]["value"] = self.armourstotal_dark

        j = 26
        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "キャラクターレベル"
        jsontext["data"]["params"][j]["value"] = self.level
        j = j + 1

        for l in range(len(self.class_name)):
            jsontext["data"]["params"].append({})
            jsontext["data"]["params"][j]["label"] = self.class_name[l] + "クラスレベル"
            jsontext["data"]["params"][j]["value"] = self.class_level[l]
            j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "状態"
        jsontext["data"]["params"][j]["value"] = ""
        j = j + 1

        outfits_main_weapon_shortattack_array = self.outfits_main_weapon_shortattack.split("+")
        outfits_sub_weapon_shortattack_array = self.outfits_sub_weapon_shortattack.split("+")
        outfits_main_weapon_longattack_array = self.outfits_main_weapon_longattack.split("+")
        outfits_sub_weapon_longattack_array = self.outfits_sub_weapon_longattack.split("+")

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = "//アクション\nムーブ:\nマイナー:\nメジャー:\n\n//リソース\n" + \
                                       "C({FP}-YY)　残りFP\n" + \
                                       "C({HP}-YY)　残りHP\n" + \
                                       "C({EN}-YY)　残りEN\n\n" + \
                                       "//防御、+0欄に修正を記入\nMG+{回避値}+0[{クリティカル値},{ファンブル値}]　近・回避\n" + \
                                       "MG+{防壁値}+0[{クリティカル値},{ファンブル値}]　遠・防壁\n" + \
                                       "C(XX-{}-0)　被ダメージ、{}内に防御属性3文字\n\n" + \
                                       "//攻撃、+0欄に修正を記入\nMG+{命中値}+0[{クリティカル値},{ファンブル値}]　近・命中\n" + \
                                       "MG+{砲撃値}+0[{クリティカル値},{ファンブル値}]　遠・砲撃\n" + \
                                       "2d6+" + outfits_main_weapon_shortattack_array[1] + "+0　" + \
                                       "〈" + outfits_main_weapon_shortattack_array[0] + "〉" + \
                                       self.outfits_main_weapon_shortname + "ダメージ\n" \
                                       "2d6+" + outfits_sub_weapon_shortattack_array[1] + "+0　" + \
                                       "〈" + outfits_sub_weapon_shortattack_array[0] + "〉" + \
                                       self.outfits_sub_weapon_shortname + "ダメージ\n" \
                                       "2d6+" + outfits_main_weapon_longattack_array[1] + "+0　" + \
                                       "〈" + outfits_main_weapon_longattack_array[0] + "〉" + \
                                       self.outfits_main_weapon_longname + "ダメージ\n" \
                                       "2d6+" + outfits_sub_weapon_longattack_array[1] + "+0　" + \
                                       "〈" + outfits_sub_weapon_longattack_array[0] + "〉" + \
                                       self.outfits_sub_weapon_longname + "ダメージ\n" + \
                                       "\n//能力値判定\nMG+{体力B}+0[{クリティカル値},{ファンブル値}]　体力判定\n" + \
                                       "MG+{反射B}+0[{クリティカル値},{ファンブル値}]　反射判定\n" + \
                                       "MG+{知覚B}+0[{クリティカル値},{ファンブル値}]　知覚判定\n" + \
                                       "MG+{理知B}+0[{クリティカル値},{ファンブル値}]　理知判定\n" + \
                                       "MG+{意志B}+0[{クリティカル値},{ファンブル値}]　意志判定\n" + \
                                       "MG+{幸運B}+0[{クリティカル値},{ファンブル値}]　幸運判定"
        command = command + "\n\n//特技"
        for i in range(len(self.skill_memo)):
            if not self.skill_name[i] == "":
                command = command + "\n特技名:" + self.skill_name[i].replace("\n", "") + "/クラス:" + self.skill_class[i] + \
                          "/レベル:" + self.skill_level[i] + "/種別:" + self.skill_type[i] + "/タイミング:" + \
                          self.skill_timing[i] + "/対象:" + self.skill_target[i] + "/射程:" + self.skill_range[i] + \
                          "/代償:" +  self.skill_cost[i] + "/備考:" + self.skill_memo[i].replace("\n", "")

        command = command + "\n\n//加護"
        for i in range(len(self.specials)):
            if not self.specials[i] == "":
                command = command + "\n加護名:" + self.specials[i].replace("\n", "") + "/効果:" + self.specials_effect[i].replace("\n", "")

        command = command + "\n\n//アイテム"
        for i in range(len(self.items)):
            if not (self.items[i] == "" or self.items_effect[i] == "特技" or "非アイテム" in self.items_effect[i]
                    or "特技" in self.items[i] or "非アイテム" in self.items[i] or "非表示" in self.items[i]):
                itemstr = self.items[i].split("*")
                command = command + "\nアイテム名:" + itemstr[0].replace("\n", "") + "/効果:" + self.items_effect[
                    i].replace("\n", "")

        if "<chatpalette_guardian_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<chatpalette_guardian_start>\n")[1]
            before_end = after_start.split("\n<chatpalette_guardian_end>")[0]
            if "<no_default_chatpalette_guardian>" in self.base_memo:
                command = before_end
            else:
                command = command + "\n\n" + before_end

        i = status_i
        if "<status_guardian_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<status_guardian_start>\n")[1]
            before_end = after_start.split("\n<status_guardian_end>")[0]
            splitted_list = before_end.split("\n<status_guardian_splitter>\n")
            for splitted in splitted_list:
                label, value, max = splitted.split(",")
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = label
                jsontext["data"]["status"][i]["value"] = int(value)
                jsontext["data"]["status"][i]["max"] = int(max)
                i = i + 1

        if "<params_guardian_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<params_guardian_start>\n")[1]
            before_end = after_start.split("\n<params_guardian_end>")[0]
            splitted_list = before_end.split("\n<params_guardian_splitter>\n")
            for splitted in splitted_list:
                label, value = splitted.split(",")
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][j]["label"] = label
                jsontext["data"]["params"][j]["value"] = value
                j = j + 1

        jsontext["data"]["commands"] = command
        jsontext["data"]["externalUrl"] = self.url
        file_name = self.guardian_name.replace("/", "_").replace("\"", "”") + "_ガーディアン駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file, ensure_ascii=False)

        print("ガーディアン駒データを生成しました")


class CharacterData():
    base_memo = ""
    url = ""
    character_name = ""
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
    specials = []
    add_fortune_point = 0
    battlesubtotal_hit = 0
    battlesubtotal_dodge = 0
    battlesubtotal_magic = 0
    battlesubtotal_countermagic = 0
    battlesubtotal_action = 0
    battlesubtotal_fp = 0
    battlesubtotal_hp = 0
    battlesubtotal_mp = 0
    battlesubtotal_attack = 0

    def input_data(self, driver, input_url):
        self.url = input_url
        self.base_memo = driver.find_element(by=By.ID, value="base.memo").get_attribute("value")
        self.character_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
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
        self.battlesubtotal_hit = driver.find_element(by=By.ID, value="battlesubtotal.hit").get_attribute("value")
        self.battlesubtotal_dodge = driver.find_element(by=By.ID, value="battlesubtotal.dodge").get_attribute("value")
        self.battlesubtotal_magic = driver.find_element(by=By.ID, value="battlesubtotal.magic").get_attribute("value")
        self.battlesubtotal_countermagic = driver.find_element(by=By.ID, value="battlesubtotal.countermagic").get_attribute("value")
        self.battlesubtotal_action = driver.find_element(by=By.ID, value="battlesubtotal.action").get_attribute("value")
        self.battlesubtotal_fp = driver.find_element(by=By.ID, value="battlesubtotal.fp").get_attribute("value")
        self.battlesubtotal_hp = driver.find_element(by=By.ID, value="battlesubtotal.hp").get_attribute("value")
        self.battlesubtotal_mp = driver.find_element(by=By.ID, value="battlesubtotal.mp").get_attribute("value")
        self.battlesubtotal_attack = driver.find_element(by=By.ID, value="battlesubtotal.attack").get_attribute("value")

        self.specials.append(driver.find_element(by=By.ID, value="specials.0.name").get_attribute("value"))

        for i in range(98):
            try:
                specialnum = i + 1
                specialstr = "specials." + str(specialnum).zfill(3) + ".name"
                self.specials.append(driver.find_element(by=By.ID, value=specialstr).get_attribute("value"))
            except:
                pass

        self.add_fortune_point = driver.find_element(by=By.ID, value="addfortunepoint").get_attribute("value")
        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name + \
               " PL:" + self.player_name + "\n"

        text = text + "【体力】" + str(self.strong_total) + "/+" + str(self.strong_bonus) + \
               "【反射】" + str(self.reflex_total) + "/+" + str(self.reflex_bonus) + \
               "【知覚】" + str(self.sense_total) + "/+" + str(self.sense_bonus) + \
               "\n【理知】" + str(self.intellect_total) + "/+" + str(self.intellect_bonus) + \
               "【意志】" + str(self.will_total) + "/+" + str(self.will_bonus) + \
               "【幸運】" + str(self.bllesing_total) + "/+" + str(self.bllesing_bonus) + "\n"

        text = text + "加護:"
        for special in self.specials:
            text = text + special + "/"
        text = text[:-1]

        text = text + "\n財産ポイント:" + self.add_fortune_point

        if "<pawntext_linkage_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<pawntext_linkage_start>\n")[1]
            before_end = after_start.split("\n<pawntext_linkage_end>")[0]
            if "<no_default_linkage_pawntext>" in self.base_memo:
                text = before_end
            else:
                text = text + "\n\n" + before_end

        print(text)

        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_リンケージテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("リンケージテキストデータを生成しました")
        self.output_pawn(text)
        #tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.battlesubtotal_action)
        jsontext["data"]["status"] = []

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][0]["label"] = "FP"
        jsontext["data"]["status"][0]["value"] = self.battlesubtotal_fp
        jsontext["data"]["status"][0]["max"] = self.battlesubtotal_fp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][1]["label"] = "HP"
        jsontext["data"]["status"][1]["value"] = self.battlesubtotal_hp
        jsontext["data"]["status"][1]["max"] = self.battlesubtotal_hp

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][2]["label"] = "EN"
        jsontext["data"]["status"][2]["value"] = self.battlesubtotal_mp
        jsontext["data"]["status"][2]["max"] = self.battlesubtotal_mp

        i = 3
        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "クリティカル値"
        jsontext["data"]["status"][i]["value"] = 12
        jsontext["data"]["status"][i]["max"] = 13
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "ファンブル値"
        jsontext["data"]["status"][i]["value"] = 2
        jsontext["data"]["status"][i]["max"] = 13
        i = i + 1
        status_i = i

        jsontext["data"]["params"] = []

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][0]["label"] = "体力基本値"
        jsontext["data"]["params"][0]["value"] = self.strong_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][1]["label"] = "反射基本値"
        jsontext["data"]["params"][1]["value"] = self.sense_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][2]["label"] = "知覚基本値"
        jsontext["data"]["params"][2]["value"] = self.strong_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][3]["label"] = "理知基本値"
        jsontext["data"]["params"][3]["value"] = self.intellect_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][4]["label"] = "意志基本値"
        jsontext["data"]["params"][4]["value"] = self.will_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][5]["label"] = "幸運基本値"
        jsontext["data"]["params"][5]["value"] = self.bllesing_total

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][6]["label"] = "体力B"
        jsontext["data"]["params"][6]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][7]["label"] = "反射B"
        jsontext["data"]["params"][7]["value"] = self.sense_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][8]["label"] = "知覚B"
        jsontext["data"]["params"][8]["value"] = self.strong_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][9]["label"] = "理知B"
        jsontext["data"]["params"][9]["value"] = self.intellect_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][10]["label"] = "意志B"
        jsontext["data"]["params"][10]["value"] = self.will_bonus

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][11]["label"] = "幸運B"
        jsontext["data"]["params"][11]["value"] = self.bllesing_bonus
        j = 12

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        jsontext["data"]["externalUrl"] = self.url
        command = "//能力値判定\n2d6+{体力B}+0[{クリティカル値},{ファンブル値}]　体力判定\n" + \
                  "2d6+{反射B}+0[{クリティカル値},{ファンブル値}]　反射判定\n" + \
                  "2d6+{知覚B}+0[{クリティカル値},{ファンブル値}]　知覚判定\n" + \
                  "2d6+{理知B}+0[{クリティカル値},{ファンブル値}]　理知判定\n" + \
                  "2d6+{意志B}+0[{クリティカル値},{ファンブル値}]　意志判定\n" + \
                  "2d6+{幸運B}+0[{クリティカル値},{ファンブル値}]　幸運判定"

        if "<chatpalette_linkage_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<chatpalette_linkage_start>\n")[1]
            before_end = after_start.split("\n<chatpalette_linkage_end>")[0]
            if "<no_default_chatpalette_linkage>" in self.base_memo:
                command = before_end
            else:
                command = command + "\n\n" + before_end

        i = status_i
        if "<status_linkage_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<status_linkage_start>\n")[1]
            before_end = after_start.split("\n<status_linkage_end>")[0]
            splitted_list = before_end.split("\n<status_linkage_splitter>\n")
            for splitted in splitted_list:
                label, value, max = splitted.split(",")
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = label
                jsontext["data"]["status"][i]["value"] = int(value)
                jsontext["data"]["status"][i]["max"] = int(max)
                i = i + 1

        if "<params_linkage_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<params_linkage_start>\n")[1]
            before_end = after_start.split("\n<params_linkage_end>")[0]
            splitted_list = before_end.split("\n<params_linkage_splitter>\n")
            for splitted in splitted_list:
                label, value = splitted.split(",")
                jsontext["data"]["params"].append({})
                jsontext["data"]["params"][j]["label"] = label
                jsontext["data"]["params"][j]["value"] = value
                j = j + 1

        jsontext["data"]["commands"] = command
        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_リンケージ駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file, ensure_ascii=False)

        print("リンケージ駒データを生成しました")


def get_data(value):
    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    character = CharacterData()
    time.sleep(5)

    character.input_data(driver, url)
    character.output_text()

    driver.quit()

    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    guardian = GuardianData()
    time.sleep(5)

    guardian.input_data(driver, url)
    guardian.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"メタリックガーディアンRPG ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1, text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/mgr/')
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