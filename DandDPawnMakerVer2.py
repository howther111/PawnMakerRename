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


def get_saving_throws(driver, timeout: int = 10) -> dict[str, dict]:
    """
    戻り値例:
    {
      "【筋力】": {"save": "0", "ability_mod": "0", "other": "", "prof_bonus": "", "proficient": False},
      ...
    }
    """
    wait = WebDriverWait(driver, timeout)

    # 「セーヴ」「能力修正」などのヘッダを持つテーブル（= セーヴ表）を特定
    table_xpath = (
        "//table[.//tr[contains(@class,'SBC')]"
        " and .//td[contains(., 'セーヴ')]"
        " and .//td[contains(., '能力修正')]]"
    )
    table = wait.until(EC.presence_of_element_located((By.XPATH, table_xpath)))

    saves = {}
    rows = table.find_elements(By.XPATH, ".//tr[contains(@class,'MWC')]")

    for r in rows:
        tds = r.find_elements(By.XPATH, "./td")
        if len(tds) < 6:
            continue

        ability = tds[0].text.strip()  # 例: "【筋力】"

        # セーヴ値（太字の DIV.A > B が入っている）
        save_val = tds[1].find_element(By.XPATH, ".//div[contains(@class,'A')]/b").text.strip()

        # 能力修正（DIV.D）
        ability_mod = tds[2].text.strip()

        other = tds[3].text.strip()
        prof_bonus = tds[4].text.strip()

        # 習熟チェック（□ が入ってる列。チェック記号が別表現ならここだけ調整）
        proficient = ("■" in tds[5].text)  # 通常は未チェックだと "□"

        saves[ability] = {
            "save": save_val,
            "ability_mod": ability_mod,
            "other": other,
            "prof_bonus": prof_bonus,
            "proficient": proficient,
        }

    return saves

def get_save_value(driver, ability_jp: str, timeout: int = 10) -> str:
    """
    ability_jp 例: "【筋力】" "【敏捷力】" "【判断力】" など
    """
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[.//tr[contains(@class,'SBC')] and .//td[contains(., 'セーヴ')] and .//td[contains(., '能力修正')]]"
        f"//tr[contains(@class,'MWC')][td[1][contains(., '{ability_jp}')]]"
        "/td[2]//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def _clean_cell_text(s: str) -> str:
    # 全角スペースや空白だけの値を空にする
    if s is None:
        return ""
    s = s.replace("\u3000", " ").strip()  # 全角スペース→半角→strip
    return s

def get_attacks(driver, timeout: int = 10) -> list[dict]:
    attacks = []
    wait = WebDriverWait(driver, timeout)

    # 表の存在を待つ（ページ読込が遅いときの保険）
    wait.until(EC.presence_of_element_located((By.XPATH, "//table[@summary='攻撃']")))

    # 攻撃行は td が5個（攻撃名がcolspan=2なのでtd数は増えない）
    rows = driver.find_elements(By.XPATH, "//table[@summary='攻撃']//tr[count(td)=5]")

    for r in rows:
        tds = r.find_elements(By.XPATH, "./td")
        if len(tds) != 5:
            continue

        attack_name  = _clean_cell_text(tds[0].text)
        attack_bonus = _clean_cell_text(tds[1].text)
        damage       = _clean_cell_text(tds[2].text)
        dmg_type     = _clean_cell_text(tds[3].text)
        note         = _clean_cell_text(tds[4].text)

        # 空行（全部空）は捨てる
        if not any([attack_name, attack_bonus, damage, dmg_type, note]):
            continue

        attacks.append({
            "attack": attack_name,
            "attack_bonus": attack_bonus,
            "damage": damage,
            "type": dmg_type,
            "note": note,
        })

    return attacks


def get_coin_total_weight(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='硬貨']"
        "//tr[td[contains(., '貨幣総重量')]]"
        "/td[2]//div[contains(@class,'C')]"
    )

    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()  # "3"


def get_coins(driver) -> dict[str, str]:
    return {
        "PP": get_coin_value(driver, "プラチナム貨"),
        "GP": get_coin_value(driver, "金貨"),
        "EP": get_coin_value(driver, "エレクトラム貨"),
        "SP": get_coin_value(driver, "銀貨"),
        "CP": get_coin_value(driver, "銅貨"),
    }


def get_coin_value(driver, label: str, timeout: int = 10) -> str:
    """
    label例:
      "プラチナム貨(PP)"
      "金貨(GP)"
      "エレクトラム貨(EP)"
      "銀貨(SP)"
      "銅貨(CP)"
    """
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='硬貨']"
        f"//tr[td[contains(., '{label}')]]"
        "/td[2]//div[contains(@class,'C')]"
    )

    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_max_hp(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        # 「ヒットポイント」表の中で「最大HP」セルを探す
        "//table[.//td[contains(., 'ヒットポイント')]]"
        "//td[contains(., '最大HP')]"
        # その「最大HP」を含む行の次の行が、数値が入った行
        "/ancestor::tr/following-sibling::tr[1]"
        # その行の1つ目のセル（最大HP側。colspan=2）から値を取る
        "/td[1]//div[contains(@class,'A')]/b"
    )

    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_inspiration(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//td[contains(., 'インスピレーション')]"
        "/following-sibling::td"
        "//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_proficiency_bonus(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//td[contains(., '習熟ボーナス')]"
        "/following-sibling::td"
        "//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_ac(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='ＡＣ']"
        "//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_speed(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='スピード']"
        "//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_initiative(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='イニシアチブ']"
        "//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_passive_perception(driver, timeout: int = 10) -> str:
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='技能']"
        "//tr[td[contains(., '受動') and contains(., '知覚')]]"
        "//div[contains(@class,'A')]/b"
    )

    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_skill_value(driver, skill_jp: str, timeout: int = 10) -> str:
    """
    skill_jp 例: "医術" / "運動" / "手先の早業" など（山括弧は不要）
    戻り値: 技能値（例 "15"）。見つからなければ例外。
    """
    wait = WebDriverWait(driver, timeout)

    xpath = (
        "//table[@summary='技能']"
        f"//tr[td[contains(., '〈{skill_jp}〉')]]"
        "/td[1]//div[contains(@class,'A')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_skill_values(driver, skills: list[str]) -> dict[str, str]:
    return {s: get_skill_value(driver, s) for s in skills}


def get_field_by_label(driver, label: str, timeout: int = 10) -> str:
    """
    例: label="キャラクター名", "属性", "プレイヤー名", "クラス", "レベル", "種族" など
    """
    wait = WebDriverWait(driver, timeout)

    # td の中に label を含むものを探し、その td 内の div.B > b を取得
    xpath = (
        f"//td[contains(normalize-space(.), '{label}')]"
        f"//div[contains(@class,'B')]/b"
    )
    el = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    return el.text.strip()


def get_abilities(driver) -> dict:
    abilities = {}
    rows = driver.find_elements(
        By.XPATH,
        "//table[@summary='能力値コメント']//tr[contains(@class,'MWC')]"
    )
    for r in rows:
        tds = r.find_elements(By.XPATH, "./td")
        if len(tds) < 3:
            continue

        score = tds[0].text.strip()                 # 11
        label = tds[1].text.strip()                 # 【筋力】 STR
        mod = tds[2].text.strip()                   # +2 等（空の場合あり）

        # STR / DEX ... を抽出（行末にある想定）
        # 例: "【筋力】\nSTR" → "STR"
        abbr = label.split()[-1].strip()
        abilities[abbr] = {"score": score, "mod": mod}
    return abilities


def get_skills(driver) -> list[dict]:
    skills = []
    rows = driver.find_elements(
        By.XPATH,
        "//table[@summary='技能']//tr[td]"  # tdを持つ行
    )

    for r in rows:
        tds = r.find_elements(By.XPATH, "./td")
        if len(tds) != 5:
            continue

        value = tds[0].text.strip()  # 技能値
        name_block = tds[1].text.strip()  # 〈医術〉\nMEDICINE
        ability = tds[2].text.strip()     # 【判】5
        prof = tds[3].text.strip()        # 4 レ など
        other = tds[4].text.strip()       # その他

        # 技能名(和)と英名を分割
        parts = name_block.splitlines()
        name_jp = parts[0].strip() if parts else ""
        name_en = parts[1].strip() if len(parts) > 1 else ""

        skills.append({
            "name_jp": name_jp,
            "name_en": name_en,
            "value": value,
            "ability": ability,
            "proficiency": prof,
            "other": other,
        })

    return skills


class Weapon:
    name = ""
    bonus = 0
    damage = ""
    element = ""
    comment = ""


class Item:
    name = ""
    weight = 0
    number = 0


class Magic:
    name = ""
    level = 0


class GuardianData:
    character_name = ""
    character_class = ""
    character_level = 0
    character_race = ""
    character_element = ""
    character_size = ""
    character_age = ""
    character_sex = ""
    character_height = ""
    character_weight = ""
    memo = ""

    player_name = ""

    str_total = 0
    str_bonus = 0
    dex_total = 0
    dex_bonus = 0
    con_total = 0
    con_bonus = 0
    int_total = 0
    int_bonus = 0
    wis_total = 0
    wis_bonus = 0
    cha_total = 0
    cha_bonus = 0
    str_save = 0
    dex_save = 0
    con_save = 0
    int_save = 0
    wis_save = 0
    cha_save = 0
    intimidation = 0
    medicine = 0
    athletics = 0
    stealth = 0
    acrobatics = 0
    insight = 0
    performance = 0
    nature = 0
    religion = 0
    survival = 0
    persuasion = 0
    investigation = 0
    perception = 0
    sleight_of_hand = 0
    animal_handling = 0
    deception = 0
    arcana = 0
    history = 0
    passive = 0

    weapon = []

    initiative = 0
    ac = 0
    speed = ""
    hp = 0
    death_save_success = 0
    death_save_fail = 0
    death_save_success_max = 3
    death_save_fail_max = 3

    inspiration = 0
    proficiency = 0

    pp = 0
    gp = 0
    ep = 0
    sp = 0
    cp = 0
    coin_weight = 0

    url = ""

    def input_data(self, driver, input_url):
        #ここを進める 2025/12/17～

        self.url = input_url
        self.character_name = get_field_by_label(driver, "キャラクター名")
        self.character_class = get_field_by_label(driver, "クラス")
        self.character_element = get_field_by_label(driver, "属性")
        self.character_race = get_field_by_label(driver, "種族")
        self.character_level = get_field_by_label(driver, "レベル")
        self.character_size = get_field_by_label(driver, "サイズ")
        self.character_age = get_field_by_label(driver, "年齢")
        self.character_sex = get_field_by_label(driver, "性別")
        self.character_height = get_field_by_label(driver, "身長")
        self.character_weight = get_field_by_label(driver, "体重")
        self.player_name = get_field_by_label(driver, "プレイヤー名")
        self.memo = get_field_by_label(driver, "メモ欄")

        abilities = get_abilities(driver)

        self.str_total = abilities["STR"]["score"]
        self.str_bonus = abilities["STR"]["mod"]
        self.dex_total = abilities["DEX"]["score"]
        self.dex_bonus = abilities["DEX"]["mod"]
        self.con_total = abilities["CON"]["score"]
        self.con_bonus = abilities["CON"]["mod"]
        self.int_total = abilities["INT"]["score"]
        self.int_bonus = abilities["INT"]["mod"]
        self.wis_total = abilities["WIS"]["score"]
        self.wis_bonus = abilities["WIS"]["mod"]
        self.cha_total = abilities["CHA"]["score"]
        self.cha_bonus = abilities["CHA"]["mod"]
        self.str_save = get_save_value(driver, "【筋力】")
        self.dex_save = get_save_value(driver, "【敏捷力】")
        self.con_save = get_save_value(driver, "【耐久力】")
        self.int_save = get_save_value(driver, "【知力】")
        self.wis_save = get_save_value(driver, "【判断力】")
        self.cha_save = get_save_value(driver, "【魅力】")

        # 取得したい技能（ご指定分）
        skills_to_get = [
            "威圧", "医術", "運動", "隠密", "軽業", "看破", "芸能", "自然", "宗教", "生存", "説得",
            "捜査", "知覚", "手先の早業", "動物使い", "ペテン", "魔法学", "歴史",
        ]

        skill_values = get_skill_values(driver, skills_to_get)

        self.intimidation = skill_values["威圧"]
        self.medicine = skill_values["医術"]
        self.athletics = skill_values["運動"]
        self.stealth = skill_values["隠密"]
        self.acrobatics = skill_values["軽業"]
        self.insight = skill_values["看破"]
        self.performance = skill_values["芸能"]
        self.nature = skill_values["自然"]
        self.religion = skill_values["宗教"]
        self.survival = skill_values["生存"]
        self.persuasion = skill_values["説得"]
        self.investigation = skill_values["捜査"]
        self.perception = skill_values["知覚"]
        self.sleight_of_hand = skill_values["手先の早業"]
        self.animal_handling = skill_values["動物使い"]
        self.deception = skill_values["ペテン"]
        self.arcana = skill_values["魔法学"]
        self.history = skill_values["歴史"]

        self.passive = get_passive_perception(driver)
        self.initiative = get_initiative(driver)
        self.ac = get_ac(driver)
        self.speed = get_speed(driver)
        self.hp = get_max_hp(driver)
        self.inspiration = get_inspiration(driver)
        self.proficiency = get_proficiency_bonus(driver)

        coins = get_coins(driver)
        self.pp = coins["PP"]
        self.gp = coins["GP"]
        self.ep = coins["EP"]
        self.sp = coins["SP"]
        self.cp = coins["CP"]
        self.coin_weight = get_coin_total_weight(driver)

        self.weapon = get_attacks(driver)

        print(self.character_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "PC:" + self.character_name +  \
                   "\nPL:" + self.player_name + \
                   "\nレベル:" + self.character_level

        text = text + "\nサイズ:" + str(self.character_size) + \
                   "\n属性:" + str(self.character_element) + \
                   "\n種族:" + str(self.character_race) + \
                   "\n年齢:" + str(self.character_age) + \
                   " 性別:" + str(self.character_sex) + \
                   "\n身長:" + str(self.character_height) + \
                   "\n体重:" + str(self.character_weight)

        if "<pawntext_start>\n" in self.memo:
            after_start = self.memo.split("<pawntext_start>\n")[1]
            before_end = after_start.split("\n<pawntext_end>")[0]
            if "<no_default_pawntext>" in self.memo:
                text = before_end
            else:
                text = text + "\n\n" + before_end

        print(text)

        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_冒険者テキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("冒険者テキストデータを生成しました")
        self.output_pawn(text)

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.character_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = int(self.initiative)
        jsontext["data"]["status"] = []

        i = 0

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "HP"
        jsontext["data"]["status"][i]["value"] = self.hp
        jsontext["data"]["status"][i]["max"] = self.hp
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "COINS_PP"
        jsontext["data"]["status"][i]["value"] = self.pp
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "COINS_GP"
        jsontext["data"]["status"][i]["value"] = self.gp
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "COINS_EP"
        jsontext["data"]["status"][i]["value"] = self.ep
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "COINS_SP"
        jsontext["data"]["status"][i]["value"] = self.sp
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "COINS_CP"
        jsontext["data"]["status"][i]["value"] = self.cp
        jsontext["data"]["status"][i]["max"] = 1000
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "死亡セーヴ_成功"
        jsontext["data"]["status"][i]["value"] = self.death_save_success
        jsontext["data"]["status"][i]["max"] = self.death_save_success_max
        i = i + 1

        jsontext["data"]["status"].append({})
        jsontext["data"]["status"][i]["label"] = "死亡セーヴ_失敗"
        jsontext["data"]["status"][i]["value"] = self.death_save_fail
        jsontext["data"]["status"][i]["max"] = self.death_save_fail_max
        i = i + 1
        status_i = i

        #弾数の管理はなし

        jsontext["data"]["params"] = []

        j = 0

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "レベル"
        jsontext["data"]["params"][j]["value"] = self.character_level
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "イニシアチブ"
        jsontext["data"]["params"][j]["value"] = self.initiative
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "AC"
        jsontext["data"]["params"][j]["value"] = self.ac
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "移動速度"
        jsontext["data"]["params"][j]["value"] = self.speed
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "筋力現在値"
        jsontext["data"]["params"][j]["value"] = self.str_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "敏捷力現在値"
        jsontext["data"]["params"][j]["value"] = self.dex_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "耐久力現在値"
        jsontext["data"]["params"][j]["value"] = self.con_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知力現在値"
        jsontext["data"]["params"][j]["value"] = self.int_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "判断力現在値"
        jsontext["data"]["params"][j]["value"] = self.wis_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魅力現在値"
        jsontext["data"]["params"][j]["value"] = self.cha_total
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "筋力修正"
        jsontext["data"]["params"][j]["value"] = self.str_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "敏捷力修正"
        jsontext["data"]["params"][j]["value"] = self.dex_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "耐久力修正"
        jsontext["data"]["params"][j]["value"] = self.con_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知力修正"
        jsontext["data"]["params"][j]["value"] = self.int_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "判断力修正"
        jsontext["data"]["params"][j]["value"] = self.wis_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魅力修正"
        jsontext["data"]["params"][j]["value"] = self.cha_bonus
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "筋力セーヴ"
        jsontext["data"]["params"][j]["value"] = self.str_save
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "敏捷力セーヴ"
        jsontext["data"]["params"][j]["value"] = self.dex_save
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "耐久力セーヴ"
        jsontext["data"]["params"][j]["value"] = self.con_save
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知力セーヴ"
        jsontext["data"]["params"][j]["value"] = self.int_save
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "判断力セーヴ"
        jsontext["data"]["params"][j]["value"] = self.wis_save
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魅力セーヴ"
        jsontext["data"]["params"][j]["value"] = self.cha_save
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "威圧"
        jsontext["data"]["params"][j]["value"] = self.intimidation
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "医術"
        jsontext["data"]["params"][j]["value"] = self.medicine
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "運動"
        jsontext["data"]["params"][j]["value"] = self.athletics
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "隠密"
        jsontext["data"]["params"][j]["value"] = self.stealth
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "軽業"
        jsontext["data"]["params"][j]["value"] = self.acrobatics
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "看破"
        jsontext["data"]["params"][j]["value"] = self.insight
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "芸能"
        jsontext["data"]["params"][j]["value"] = self.performance
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "自然"
        jsontext["data"]["params"][j]["value"] = self.nature
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "宗教"
        jsontext["data"]["params"][j]["value"] = self.religion
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "生存"
        jsontext["data"]["params"][j]["value"] = self.survival
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "説得"
        jsontext["data"]["params"][j]["value"] = self.persuasion
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "捜査"
        jsontext["data"]["params"][j]["value"] = self.investigation
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "知覚"
        jsontext["data"]["params"][j]["value"] = self.perception
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "手先の早業"
        jsontext["data"]["params"][j]["value"] = self.sleight_of_hand
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "動物使い"
        jsontext["data"]["params"][j]["value"] = self.animal_handling
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "ペテン"
        jsontext["data"]["params"][j]["value"] = self.deception
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "魔法学"
        jsontext["data"]["params"][j]["value"] = self.arcana
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "歴史"
        jsontext["data"]["params"][j]["value"] = self.history
        j = j + 1

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][j]["label"] = "状態"
        jsontext["data"]["params"][j]["value"] = ""
        j = j + 1

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = "//イニシアチブ==========\n"
        command = command + "1d20+{イニシアチブ} ▼イニシアチブ\n"
        command = command + "\n//命中判定==========\n"
        for wpn in self.weapon:
            if not wpn["attack"] == "攻撃":
                command = command + "1d20+" + wpn["attack_bonus"] + " ▼" + wpn["attack"] + "での攻撃ロール\n"
                command = command + wpn["damage"] + " ▼" + wpn["attack"] + \
                "でのダメージロール[" + wpn["type"] + "]" + wpn["note"] + "\n"

        command = command + "\n//能力値判定==========\n"
        command = command + "1d20{筋力修正} ▼【筋力】能力値判定\n"
        command = command + "1d20{敏捷力修正} ▼【敏捷力】能力値判定\n"
        command = command + "1d20{耐久力修正} ▼【耐久力】能力値判定\n"
        command = command + "1d20{知力修正} ▼【知力】能力値判定\n"
        command = command + "1d20{判断力修正} ▼【判断力】能力値判定\n"
        command = command + "1d20{魅力修正} ▼【魅力】能力値判定\n"

        command = command + "\n//セーヴィング・スロー==========\n"
        command = command + "1d20+{筋力セーヴ} ▼【筋力】セーヴィングスロー\n"
        command = command + "1d20+{敏捷力セーヴ} ▼【敏捷力】セーヴィングスロー\n"
        command = command + "1d20+{耐久力セーヴ} ▼【耐久力】セーヴィングスロー\n"
        command = command + "1d20+{知力セーヴ} ▼【知力】セーヴィングスロー\n"
        command = command + "1d20+{判断力セーヴ} ▼【判断力】セーヴィングスロー\n"
        command = command + "1d20+{魅力セーヴ} ▼【魅力】セーヴィングスロー\n"

        command = command + "\n//技能==========\n"
        command = command + "1d20+{威圧} 〈威圧〉【魅】技能判定\n"
        command = command + "1d20+{医術} 〈医術〉【判】技能判定\n"
        command = command + "1d20+{運動} 〈運動〉【筋】技能判定\n"
        command = command + "1d20+{隠密} 〈隠密〉【敏】技能判定\n"
        command = command + "1d20+{軽業} 〈軽業〉【敏】技能判定\n"
        command = command + "1d20+{看破} 〈看破〉【判】技能判定\n"
        command = command + "1d20+{芸能} 〈芸能〉【魅】技能判定\n"
        command = command + "1d20+{自然} 〈自然〉【知】技能判定\n"
        command = command + "1d20+{宗教} 〈宗教〉【知】技能判定\n"
        command = command + "1d20+{生存} 〈生存〉【判】技能判定\n"
        command = command + "1d20+{説得} 〈説得〉【魅】技能判定\n"
        command = command + "1d20+{捜査} 〈捜査〉【知】技能判定\n"
        command = command + "1d20+{知覚} 〈知覚〉【判】技能判定\n"
        command = command + "1d20+{手先の早業} 〈手先の早業〉【敏】技能判定\n"
        command = command + "1d20+{動物使い} 〈動物使い〉【判】技能判定\n"
        command = command + "1d20+{ペテン} 〈ペテン〉【魅】技能判定\n"
        command = command + "1d20+{魔法学} 〈魔法学〉【知】技能判定\n"
        command = command + "1d20+{歴史} 〈歴史〉【知】技能判定"

        if "<chatpalette_start>\n" in self.memo:
            after_start = self.memo.split("<chatpalette_start>\n")[1]
            before_end = after_start.split("\n<chatpalette_end>")[0]
            if "<no_default_chatpalette>" in self.memo:
                command = before_end
            else:
                command = command + "\n\n" + before_end

        i = status_i
        if "<status_start>\n" in self.memo:
            after_start = self.memo.split("<status_start>\n")[1]
            before_end = after_start.split("\n<status_end>")[0]
            splitted_list = before_end.split("\n<status_splitter>\n")
            for splitted in splitted_list:
                label, value, max = splitted.split(",")
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = label
                jsontext["data"]["status"][i]["value"] = int(value)
                jsontext["data"]["status"][i]["max"] = int(max)
                i = i + 1

        if "<params_start>\n" in self.memo:
            after_start = self.memo.split("<params_start>\n")[1]
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
        file_name = self.character_name.replace("/", "_").replace("\"", "”") + "_冒険者駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as file:  # 第二引数：writableオプションを指定
            json.dump(jsontext, file, ensure_ascii=False)

        print("冒険者駒データを生成しました")


def get_data(value):

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
    root.title(u"ダンジョンズ&ドラゴンズ5E ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1,text=u'キャラクターシートURL\nhttps://dndjp.sakura.ne.jp/LIST.php')
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