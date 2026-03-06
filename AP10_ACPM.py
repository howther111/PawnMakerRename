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

class ArmoredCoreData():
    url = ""
    base_memo = ""
    player_name = ""
    cord_name = ""
    ac_name = ""
    coam_sum = 0
    level = 0
    legs_type = ""
    core_oneline_point = 0
    core_line_num = 0
    arms_oneline_point = 0
    arms_line_num = 0
    legs_oneline_point = 0
    legs_line_num = 0
    weapon_r_name = ""
    weapon_r_category = ""
    weapon_r_oneline_point = 0
    weapon_r_line_num = 0
    weapon_r_mod = 0
    weapon_r_1_range = 0
    weapon_r_1_cost_dice = ""
    weapon_r_1_cost_bullets = ""
    weapon_r_1_element = ""
    weapon_r_1_attacktype = ""
    weapon_r_1_hitnum = 0
    weapon_r_1_attack = 0
    weapon_r_2_range = 0
    weapon_r_2_cost_dice = ""
    weapon_r_2_cost_bullets = ""
    weapon_r_2_element = ""
    weapon_r_2_attacktype = ""
    weapon_r_2_hitnum = 0
    weapon_r_2_attack = 0
    weapon_r_3_range = 0
    weapon_r_3_cost_dice = ""
    weapon_r_3_cost_bullets = ""
    weapon_r_3_element = 0
    weapon_r_3_attacktype = ""
    weapon_r_3_hitnum = 0
    weapon_r_3_attack = 0
    weapon_l_name = ""
    weapon_l_category = ""
    weapon_l_oneline_point = 0
    weapon_l_line_num = 0
    weapon_l_mod = 0
    weapon_l_1_range = 0
    weapon_l_1_cost_dice = ""
    weapon_l_1_cost_bullets = ""
    weapon_l_1_element = ""
    weapon_l_1_attacktype = ""
    weapon_l_1_hitnum = 0
    weapon_l_1_attack = 0
    weapon_l_2_range = 0
    weapon_l_2_cost_dice = ""
    weapon_l_2_cost_bullets = ""
    weapon_l_2_element = ""
    weapon_l_2_attacktype = ""
    weapon_l_2_hitnum = 0
    weapon_l_2_attack = 0
    weapon_l_3_range = 0
    weapon_l_3_cost_dice = ""
    weapon_l_3_cost_bullets = ""
    weapon_l_3_element = 0
    weapon_l_3_attacktype = ""
    weapon_l_3_hitnum = 0
    weapon_l_3_attack = 0
    shoulder_r_name = ""
    shoulder_r_category = ""
    shoulder_r_oneline_point = 0
    shoulder_r_line_num = 0
    shoulder_r_mod = 0
    shoulder_r_1_range = 0
    shoulder_r_1_cost_dice = ""
    shoulder_r_1_cost_bullets = ""
    shoulder_r_1_element = ""
    shoulder_r_1_attacktype = ""
    shoulder_r_1_hitnum = 0
    shoulder_r_1_attack = 0
    shoulder_r_2_range = 0
    shoulder_r_2_cost_dice = ""
    shoulder_r_2_cost_bullets = ""
    shoulder_r_2_element = ""
    shoulder_r_2_attacktype = ""
    shoulder_r_2_hitnum = 0
    shoulder_r_2_attack = 0
    shoulder_r_3_range = 0
    shoulder_r_3_cost_dice = ""
    shoulder_r_3_cost_bullets = ""
    shoulder_r_3_element = 0
    shoulder_r_3_attacktype = ""
    shoulder_r_3_hitnum = 0
    shoulder_r_3_attack = 0
    shoulder_l_name = ""
    shoulder_l_category = ""
    shoulder_l_oneline_point = 0
    shoulder_l_line_num = 0
    shoulder_l_mod = 0
    shoulder_l_1_range = 0
    shoulder_l_1_cost_dice = ""
    shoulder_l_1_cost_bullets = ""
    shoulder_l_1_element = ""
    shoulder_l_1_attacktype = ""
    shoulder_l_1_hitnum = 0
    shoulder_l_1_attack = 0
    shoulder_l_2_range = 0
    shoulder_l_2_cost_dice = ""
    shoulder_l_2_cost_bullets = ""
    shoulder_l_2_element = ""
    shoulder_l_2_attacktype = ""
    shoulder_l_2_hitnum = 0
    shoulder_l_2_attack = 0
    shoulder_l_3_range = 0
    shoulder_l_3_cost_dice = ""
    shoulder_l_3_cost_bullets = ""
    shoulder_l_3_element = 0
    shoulder_l_3_attacktype = ""
    shoulder_l_3_hitnum = 0
    shoulder_l_3_attack = 0
    en_dice_max = 0
    en_dice_turnstart = 0
    en_dice_playerstart = 0
    move_cost = 0
    dodge_cost = 0
    incident = 0
    search = 0
    hacking = 0
    maneuver = 0

    defense_bullet = 0
    defense_explosion = 0
    defense_energy = 0

    skill_name = []
    skill_type = []
    skill_timing = []
    skill_cost = []
    skill_effect = []

    weapon_r_skill = ""
    weapon_l_skill = ""
    shoulder_r_skill = ""
    shoulder_l_skill = ""

    def input_data(self, driver, input_url):
        self.url = input_url
        self.base_memo = driver.find_element(by=By.ID, value="base.memo").get_attribute("value")
        self.player_name = driver.find_element(by=By.ID, value="base.player").get_attribute("value")
        self.cord_name = driver.find_element(by=By.ID, value="base.name").get_attribute("value")
        self.ac_name = driver.find_element(by=By.ID, value="base.acname").get_attribute("value")
        self.coam_sum = driver.find_element(by=By.ID, value="base.totalcoam").get_attribute("value")
        self.level = driver.find_element(by=By.ID, value="base.level").get_attribute("textContent")
        self.legs_type = driver.find_element(by=By.ID, value="parts.legs.type").get_attribute("value")
        self.core_oneline_point = driver.find_element(by=By.ID, value="parts.core.ap.point").get_attribute("value")
        self.core_line_num = driver.find_element(by=By.ID, value="parts.core.ap.line").get_attribute("value")
        self.arms_oneline_point = driver.find_element(by=By.ID, value="parts.arms.ap.point").get_attribute("value")
        self.arms_line_num = driver.find_element(by=By.ID, value="parts.arms.ap.line").get_attribute("value")
        self.legs_oneline_point = driver.find_element(by=By.ID, value="parts.legs.ap.point").get_attribute("value")
        self.legs_line_num = driver.find_element(by=By.ID, value="parts.legs.ap.line").get_attribute("value")
        self.weapon_r_name = driver.find_element(by=By.ID, value="weapons.armsright.name").get_attribute("textContent")
        self.weapon_r_category = driver.find_element(by=By.ID, value="weapons.armsright.category").get_attribute("value")
        self.weapon_r_oneline_point = driver.find_element(by=By.ID, value="weapons.armsright.bullets.number").get_attribute("value")
        self.weapon_r_line_num = driver.find_element(by=By.ID, value="weapons.armsright.bullets.line").get_attribute("value")
        self.weapon_r_mod = driver.find_element(by=By.ID, value="weapons.armsright.attackmod.total").get_attribute("textContent")
        self.weapon_r_1_range = driver.find_element(by=By.ID, value="weapons.armsright.method1.range").get_attribute("value")
        self.weapon_r_1_cost_dice = driver.find_element(by=By.ID, value="weapons.armsright.method1.dice").get_attribute("value")
        self.weapon_r_1_cost_bullets = driver.find_element(by=By.ID, value="weapons.armsright.method1.bullets").get_attribute("value")
        self.weapon_r_1_element = driver.find_element(by=By.ID, value="weapons.armsright.method1.damagetype").get_attribute("value")
        self.weapon_r_1_attacktype = driver.find_element(by=By.ID, value="weapons.armsright.method1.attacktype").get_attribute("value")
        self.weapon_r_1_hitnum = driver.find_element(by=By.ID, value="weapons.armsright.method1.hit").get_attribute("value")
        self.weapon_r_1_attack = driver.find_element(by=By.ID, value="weapons.armsright.method1.attacktotal").get_attribute("textContent")
        self.weapon_r_2_range = driver.find_element(by=By.ID, value="weapons.armsright.method2.range").get_attribute(
            "value")
        self.weapon_r_2_cost_dice = driver.find_element(by=By.ID, value="weapons.armsright.method2.dice").get_attribute(
            "value")
        self.weapon_r_2_cost_bullets = driver.find_element(by=By.ID,
                                                           value="weapons.armsright.method2.bullets").get_attribute(
            "value")
        self.weapon_r_2_element = driver.find_element(by=By.ID,
                                                      value="weapons.armsright.method2.damagetype").get_attribute(
            "value")
        self.weapon_r_2_attacktype = driver.find_element(by=By.ID,
                                                         value="weapons.armsright.method2.attacktype").get_attribute(
            "value")
        self.weapon_r_2_hitnum = driver.find_element(by=By.ID, value="weapons.armsright.method2.hit").get_attribute(
            "value")
        self.weapon_r_2_attack = driver.find_element(by=By.ID,
                                                     value="weapons.armsright.method2.attacktotal").get_attribute(
            "textContent")

        self.weapon_r_3_range = driver.find_element(by=By.ID, value="weapons.armsright.method3.range").get_attribute(
            "value")
        self.weapon_r_3_cost_dice = driver.find_element(by=By.ID, value="weapons.armsright.method3.dice").get_attribute(
            "value")
        self.weapon_r_3_cost_bullets = driver.find_element(by=By.ID,
                                                           value="weapons.armsright.method3.bullets").get_attribute(
            "value")
        self.weapon_r_3_element = driver.find_element(by=By.ID,
                                                      value="weapons.armsright.method3.damagetype").get_attribute(
            "value")
        self.weapon_r_3_attacktype = driver.find_element(by=By.ID,
                                                         value="weapons.armsright.method3.attacktype").get_attribute(
            "value")
        self.weapon_r_3_hitnum = driver.find_element(by=By.ID, value="weapons.armsright.method3.hit").get_attribute(
            "value")
        self.weapon_r_3_attack = driver.find_element(by=By.ID,
                                                     value="weapons.armsright.method3.attacktotal").get_attribute(
            "textContent")

        self.weapon_l_name = driver.find_element(by=By.ID, value="weapons.armsleft.name").get_attribute("textContent")
        self.weapon_l_category = driver.find_element(by=By.ID, value="weapons.armsleft.category").get_attribute(
            "value")
        self.weapon_l_oneline_point = driver.find_element(by=By.ID,
                                                          value="weapons.armsleft.bullets.number").get_attribute(
            "value")
        self.weapon_l_line_num = driver.find_element(by=By.ID, value="weapons.armsleft.bullets.line").get_attribute(
            "value")
        self.weapon_l_mod = driver.find_element(by=By.ID, value="weapons.armsleft.attackmod.total").get_attribute(
            "textContent")
        self.weapon_l_1_range = driver.find_element(by=By.ID, value="weapons.armsleft.method1.range").get_attribute(
            "value")
        self.weapon_l_1_cost_dice = driver.find_element(by=By.ID, value="weapons.armsleft.method1.dice").get_attribute(
            "value")
        self.weapon_l_1_cost_bullets = driver.find_element(by=By.ID,
                                                           value="weapons.armsleft.method1.bullets").get_attribute(
            "value")
        self.weapon_l_1_element = driver.find_element(by=By.ID,
                                                      value="weapons.armsleft.method1.damagetype").get_attribute(
            "value")
        self.weapon_l_1_attacktype = driver.find_element(by=By.ID,
                                                         value="weapons.armsleft.method1.attacktype").get_attribute(
            "value")
        self.weapon_l_1_hitnum = driver.find_element(by=By.ID, value="weapons.armsleft.method1.hit").get_attribute(
            "value")
        self.weapon_l_1_attack = driver.find_element(by=By.ID,
                                                     value="weapons.armsleft.method1.attacktotal").get_attribute("textContent")
        self.weapon_l_2_range = driver.find_element(by=By.ID, value="weapons.armsleft.method2.range").get_attribute(
            "value")
        self.weapon_l_2_cost_dice = driver.find_element(by=By.ID, value="weapons.armsleft.method2.dice").get_attribute(
            "value")
        self.weapon_l_2_cost_bullets = driver.find_element(by=By.ID,
                                                           value="weapons.armsleft.method2.bullets").get_attribute(
            "value")
        self.weapon_l_2_element = driver.find_element(by=By.ID,
                                                      value="weapons.armsleft.method2.damagetype").get_attribute(
            "value")
        self.weapon_l_2_attacktype = driver.find_element(by=By.ID,
                                                         value="weapons.armsleft.method2.attacktype").get_attribute(
            "value")
        self.weapon_l_2_hitnum = driver.find_element(by=By.ID, value="weapons.armsleft.method2.hit").get_attribute(
            "value")
        self.weapon_l_2_attack = driver.find_element(by=By.ID,
                                                     value="weapons.armsleft.method2.attacktotal").get_attribute(
            "textContent")

        self.weapon_l_3_range = driver.find_element(by=By.ID, value="weapons.armsleft.method3.range").get_attribute(
            "value")
        self.weapon_l_3_cost_dice = driver.find_element(by=By.ID, value="weapons.armsleft.method3.dice").get_attribute(
            "value")
        self.weapon_l_3_cost_bullets = driver.find_element(by=By.ID,
                                                           value="weapons.armsleft.method3.bullets").get_attribute(
            "value")
        self.weapon_l_3_element = driver.find_element(by=By.ID,
                                                      value="weapons.armsleft.method3.damagetype").get_attribute(
            "value")
        self.weapon_l_3_attacktype = driver.find_element(by=By.ID,
                                                         value="weapons.armsleft.method3.attacktype").get_attribute(
            "value")
        self.weapon_l_3_hitnum = driver.find_element(by=By.ID, value="weapons.armsleft.method3.hit").get_attribute(
            "value")
        self.weapon_l_3_attack = driver.find_element(by=By.ID,
                                                     value="weapons.armsleft.method3.attacktotal").get_attribute(
            "textContent")
        self.shoulder_r_name = driver.find_element(by=By.ID, value="weapons.shoulderright.name").get_attribute("textContent")
        self.shoulder_r_category = driver.find_element(by=By.ID, value="weapons.shoulderright.category").get_attribute(
            "value")
        self.shoulder_r_oneline_point = driver.find_element(by=By.ID,
                                                            value="weapons.shoulderright.bullets.number").get_attribute(
            "value")
        self.shoulder_r_line_num = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.bullets.line").get_attribute(
            "value")
        self.shoulder_r_mod = driver.find_element(by=By.ID,
                                                  value="weapons.shoulderright.attackmod.total").get_attribute(
            "textContent")
        self.shoulder_r_1_range = driver.find_element(by=By.ID,
                                                      value="weapons.shoulderright.method1.range").get_attribute(
            "value")
        self.shoulder_r_1_cost_dice = driver.find_element(by=By.ID,
                                                          value="weapons.shoulderright.method1.dice").get_attribute(
            "value")
        self.shoulder_r_1_cost_bullets = driver.find_element(by=By.ID,
                                                             value="weapons.shoulderright.method1.bullets").get_attribute(
            "value")
        self.shoulder_r_1_element = driver.find_element(by=By.ID,
                                                        value="weapons.shoulderright.method1.damagetype").get_attribute(
            "value")
        self.shoulder_r_1_attacktype = driver.find_element(by=By.ID,
                                                           value="weapons.shoulderright.method1.attacktype").get_attribute(
            "value")
        self.shoulder_r_1_hitnum = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.method1.hit").get_attribute(
            "value")
        self.shoulder_r_1_attack = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.method1.attacktotal").get_attribute(
            "textContent")
        self.shoulder_r_2_range = driver.find_element(by=By.ID,
                                                      value="weapons.shoulderright.method2.range").get_attribute(
            "value")
        self.shoulder_r_2_cost_dice = driver.find_element(by=By.ID,
                                                          value="weapons.shoulderright.method2.dice").get_attribute(
            "value")
        self.shoulder_r_2_cost_bullets = driver.find_element(by=By.ID,
                                                             value="weapons.shoulderright.method2.bullets").get_attribute(
            "value")
        self.shoulder_r_2_element = driver.find_element(by=By.ID,
                                                        value="weapons.shoulderright.method2.damagetype").get_attribute(
            "value")
        self.shoulder_r_2_attacktype = driver.find_element(by=By.ID,
                                                           value="weapons.shoulderright.method2.attacktype").get_attribute(
            "value")
        self.shoulder_r_2_hitnum = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.method2.hit").get_attribute(
            "value")
        self.shoulder_r_2_attack = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.method2.attacktotal").get_attribute(
            "textContent")

        self.shoulder_r_3_range = driver.find_element(by=By.ID,
                                                      value="weapons.shoulderright.method3.range").get_attribute(
            "value")
        self.shoulder_r_3_cost_dice = driver.find_element(by=By.ID,
                                                          value="weapons.shoulderright.method3.dice").get_attribute(
            "value")
        self.shoulder_r_3_cost_bullets = driver.find_element(by=By.ID,
                                                             value="weapons.shoulderright.method3.bullets").get_attribute(
            "value")
        self.shoulder_r_3_element = driver.find_element(by=By.ID,
                                                        value="weapons.shoulderright.method3.damagetype").get_attribute(
            "value")
        self.shoulder_r_3_attacktype = driver.find_element(by=By.ID,
                                                           value="weapons.shoulderright.method3.attacktype").get_attribute(
            "value")
        self.shoulder_r_3_hitnum = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.method3.hit").get_attribute(
            "value")
        self.shoulder_r_3_attack = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderright.method3.attacktotal").get_attribute(
            "textContent")

        self.shoulder_l_name = driver.find_element(by=By.ID, value="weapons.shoulderleft.name").get_attribute("textContent")
        self.shoulder_l_category = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.category").get_attribute(
            "value")
        self.shoulder_l_oneline_point = driver.find_element(by=By.ID,
                                                            value="weapons.shoulderleft.bullets.number").get_attribute(
            "value")
        self.shoulder_l_line_num = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.bullets.line").get_attribute(
            "value")
        self.shoulder_l_mod = driver.find_element(by=By.ID,
                                                  value="weapons.shoulderleft.attackmod.total").get_attribute(
            "textContent")
        self.shoulder_l_1_range = driver.find_element(by=By.ID,
                                                      value="weapons.shoulderleft.method1.range").get_attribute(
            "value")
        self.shoulder_l_1_cost_dice = driver.find_element(by=By.ID,
                                                          value="weapons.shoulderleft.method1.dice").get_attribute(
            "value")
        self.shoulder_l_1_cost_bullets = driver.find_element(by=By.ID,
                                                             value="weapons.shoulderleft.method1.bullets").get_attribute(
            "value")
        self.shoulder_l_1_element = driver.find_element(by=By.ID,
                                                        value="weapons.shoulderleft.method1.damagetype").get_attribute(
            "value")
        self.shoulder_l_1_attacktype = driver.find_element(by=By.ID,
                                                           value="weapons.shoulderleft.method1.attacktype").get_attribute(
            "value")
        self.shoulder_l_1_hitnum = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.method1.hit").get_attribute(
            "value")
        self.shoulder_l_1_attack = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.method1.attacktotal").get_attribute(
            "textContent")
        self.shoulder_l_2_range = driver.find_element(by=By.ID,
                                                      value="weapons.shoulderleft.method2.range").get_attribute(
            "value")
        self.shoulder_l_2_cost_dice = driver.find_element(by=By.ID,
                                                          value="weapons.shoulderleft.method2.dice").get_attribute(
            "value")
        self.shoulder_l_2_cost_bullets = driver.find_element(by=By.ID,
                                                             value="weapons.shoulderleft.method2.bullets").get_attribute(
            "value")
        self.shoulder_l_2_element = driver.find_element(by=By.ID,
                                                        value="weapons.shoulderleft.method2.damagetype").get_attribute(
            "value")
        self.shoulder_l_2_attacktype = driver.find_element(by=By.ID,
                                                           value="weapons.shoulderleft.method2.attacktype").get_attribute(
            "value")
        self.shoulder_l_2_hitnum = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.method2.hit").get_attribute(
            "value")
        self.shoulder_l_2_attack = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.method2.attacktotal").get_attribute(
            "textContent")

        self.shoulder_l_3_range = driver.find_element(by=By.ID,
                                                      value="weapons.shoulderleft.method3.range").get_attribute(
            "value")
        self.shoulder_l_3_cost_dice = driver.find_element(by=By.ID,
                                                          value="weapons.shoulderleft.method3.dice").get_attribute(
            "value")
        self.shoulder_l_3_cost_bullets = driver.find_element(by=By.ID,
                                                             value="weapons.shoulderleft.method3.bullets").get_attribute(
            "value")
        self.shoulder_l_3_element = driver.find_element(by=By.ID,
                                                        value="weapons.shoulderleft.method3.damagetype").get_attribute(
            "value")
        self.shoulder_l_3_attacktype = driver.find_element(by=By.ID,
                                                           value="weapons.shoulderleft.method3.attacktype").get_attribute(
            "value")
        self.shoulder_l_3_hitnum = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.method3.hit").get_attribute(
            "value")
        self.shoulder_l_3_attack = driver.find_element(by=By.ID,
                                                       value="weapons.shoulderleft.method3.attacktotal").get_attribute(
            "textContent")
        self.en_dice_max = driver.find_element(by=By.ID,
                                                       value="mobility.max.total").get_attribute(
            "textContent")
        self.en_dice_turnstart = driver.find_element(by=By.ID,
                                                       value="mobility.turn.total").get_attribute(
            "textContent")
        self.en_dice_playerstart = driver.find_element(by=By.ID,
                                                       value="mobility.myturn.total").get_attribute(
            "textContent")
        self.move_cost = driver.find_element(by=By.ID,
                                                       value="mobility.movecost.total").get_attribute(
            "textContent")
        self.dodge_cost = driver.find_element(by=By.ID,
                                                       value="mobility.dodgecost.total").get_attribute(
            "textContent")
        self.incident = driver.find_element(by=By.ID,
                                                       value="judge.incident.total").get_attribute(
            "textContent")
        self.search = driver.find_element(by=By.ID,
                                                       value="judge.search.total").get_attribute(
            "textContent")
        self.hacking = driver.find_element(by=By.ID,
                                                       value="judge.hacking.total").get_attribute(
            "textContent")
        self.maneuver = driver.find_element(by=By.ID,
                                                       value="judge.maneuver.total").get_attribute(
            "textContent")

        self.defense_bullet = driver.find_element(by=By.ID,
                                                       value="defense.bullet").get_attribute(
            "value")
        self.defense_explosion = driver.find_element(by=By.ID,
                                                       value="defense.explosion").get_attribute(
            "value")
        self.defense_energy = driver.find_element(by=By.ID,
                                                       value="defense.energy").get_attribute(
            "value")

        skillnamestr = "skills.0.name"
        self.skill_name.append(driver.find_element(by=By.ID, value=skillnamestr).get_attribute("value"))

        skilltypestr = "skills.0.type"
        self.skill_type.append(driver.find_element(by=By.ID, value=skilltypestr).get_attribute("value"))

        skilltimingstr = "skills.0.timing"
        self.skill_timing.append(driver.find_element(by=By.ID, value=skilltimingstr).get_attribute("value"))

        skillcoststr = "skills.0.cost"
        self.skill_cost.append(driver.find_element(by=By.ID, value=skillcoststr).get_attribute("value"))

        skilleffectstr = "skills.0.effect"
        self.skill_effect.append(driver.find_element(by=By.ID, value=skilleffectstr).get_attribute("value"))

        for i in range(998):
            try:
                skillnum = i + 1
                skillnamestr = "skills." + str(skillnum).zfill(3) + ".name"
                self.skill_name.append(driver.find_element(by=By.ID, value=skillnamestr).get_attribute("value"))

                skilltypestr = "skills." + str(skillnum).zfill(3) + ".type"
                self.skill_type.append(driver.find_element(by=By.ID, value=skilltypestr).get_attribute("value"))

                skilltimingstr = "skills." + str(skillnum).zfill(3) + ".timing"
                self.skill_timing.append(driver.find_element(by=By.ID, value=skilltimingstr).get_attribute("value"))

                skillcoststr = "skills." + str(skillnum).zfill(3) + ".cost"
                self.skill_cost.append(driver.find_element(by=By.ID, value=skillcoststr).get_attribute("value"))

                skilleffectstr = "skills." + str(skillnum).zfill(3) + ".effect"
                self.skill_effect.append(driver.find_element(by=By.ID, value=skilleffectstr).get_attribute("value"))
            except:
                break

        self.weapon_r_skill = driver.find_element(by=By.ID, value="weapons.armsright.skill").get_attribute("value")
        self.weapon_l_skill = driver.find_element(by=By.ID, value="weapons.armsleft.skill").get_attribute("value")
        self.shoulder_r_skill = driver.find_element(by=By.ID, value="weapons.shoulderright.skill").get_attribute("value")
        self.shoulder_l_skill = driver.find_element(by=By.ID, value="weapons.shoulderleft.skill").get_attribute("value")

        print(self.ac_name)

    def output_text(self):
        # 駒のテキストデータを出力する
        text = "AC:" + self.ac_name + "\n" + \
                   "コードネーム:" + self.cord_name +  \
                   " PL:" + self.player_name + "\n" + \
                   "合計COAM:" + none_to_str(self.coam_sum) + \
                   " 部隊レベル:" + none_to_str(self.level)

        text = text + "\n【ENダイス最大値】" + none_to_str(self.en_dice_max) + \
                   "\n【ターン開始時ENダイス】" + none_to_str(self.en_dice_turnstart) + \
                   "\n【手番開始時ENダイス】" + none_to_str(self.en_dice_playerstart) + \
                   "\n【移動コスト】" + none_to_str(self.move_cost) + \
                   "【回避コスト】" + none_to_str(self.dodge_cost) + \
                   "\n【対システム障害】2D+" + none_to_str(self.incident) + \
                   "【サーチ】2D+" + none_to_str(self.search) + \
                   "\n【ハッキング】2D+" + none_to_str(self.hacking) + \
                   "【マニューバ】2D+" + none_to_str(self.maneuver)

        text = text + "\n[*]腕武装R:" + none_to_str(self.weapon_r_name) + \
               "\nカテゴリー:" + none_to_str(self.weapon_r_category) + \
               "/威力補正:" + none_to_str(self.weapon_r_mod) + \
               "/弾数:" + none_to_str(self.weapon_r_oneline_point) + \
               "×" + none_to_str(self.weapon_r_line_num) + "Line"

        if not none_to_str(self.weapon_r_1_range) == "":
            text = text + "\n①レンジ:" + none_to_str(self.weapon_r_1_range) + \
               "/ダイスコスト:" + none_to_str(self.weapon_r_1_cost_dice) + \
               "/弾数コスト:" + none_to_str(self.weapon_r_1_cost_bullets) + \
               "/属性:" + none_to_str(self.weapon_r_1_element) + \
               "/火力タイプ:" + none_to_str(self.weapon_r_1_attacktype) + \
               "/Hit数:" + none_to_str(self.weapon_r_1_hitnum) + \
               "/威力:" + none_to_str(self.weapon_r_1_attack)

        if not none_to_str(self.weapon_r_2_range) == "":
            text = text + "\n②レンジ:" + none_to_str(self.weapon_r_2_range) + \
               "/ダイスコスト:" + none_to_str(self.weapon_r_2_cost_dice) + \
               "/弾数コスト:" + none_to_str(self.weapon_r_2_cost_bullets) + \
               "/属性:" + none_to_str(self.weapon_r_2_element) + \
               "/火力タイプ:" + none_to_str(self.weapon_r_2_attacktype) + \
               "/Hit数:" + none_to_str(self.weapon_r_2_hitnum) + \
               "/威力:" + none_to_str(self.weapon_r_2_attack)

        if not none_to_str(self.weapon_r_3_range) == "":
            text = text + "\n③レンジ:" + none_to_str(self.weapon_r_3_range) + \
               "/ダイスコスト:" + none_to_str(self.weapon_r_3_cost_dice) + \
               "/弾数コスト:" + none_to_str(self.weapon_r_3_cost_bullets) + \
               "/属性:" + none_to_str(self.weapon_r_3_element) + \
               "/火力タイプ:" + none_to_str(self.weapon_r_3_attacktype) + \
               "/Hit数:" + none_to_str(self.weapon_r_3_hitnum) + \
               "/威力:" + none_to_str(self.weapon_r_3_attack)

        text = text + "\n[*]腕武装L+:" + none_to_str(self.weapon_l_name) + \
               "\nカテゴリー:" + none_to_str(self.weapon_l_category) + \
               "/威力補正:" + none_to_str(self.weapon_l_mod) + \
               "/弾数:" + none_to_str(self.weapon_l_oneline_point) + \
               "×" + none_to_str(self.weapon_l_line_num) + "Line"

        if not none_to_str(self.weapon_l_1_range) == "":
            text = text + "\n①レンジ:" + none_to_str(self.weapon_l_1_range) + \
                   "/ダイスコスト:" + none_to_str(self.weapon_l_1_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.weapon_l_1_cost_bullets) + \
                   "/属性:" + none_to_str(self.weapon_l_1_element) + \
                   "/火力タイプ:" + none_to_str(self.weapon_l_1_attacktype) + \
                   "/Hit数:" + none_to_str(self.weapon_l_1_hitnum) + \
                   "/威力:" + none_to_str(self.weapon_l_1_attack)

        if not none_to_str(self.weapon_l_2_range) == "":
            text = text + "\n②レンジ:" + none_to_str(self.weapon_l_2_range) + \
                   "/ダイスコスト:" + none_to_str(self.weapon_l_2_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.weapon_l_2_cost_bullets) + \
                   "/属性:" + none_to_str(self.weapon_l_2_element) + \
                   "/火力タイプ:" + none_to_str(self.weapon_l_2_attacktype) + \
                   "/Hit数:" + none_to_str(self.weapon_l_2_hitnum) + \
                   "/威力:" + none_to_str(self.weapon_l_2_attack)

        if not none_to_str(self.weapon_l_3_range) == "":
            text = text + "\n③レンジ:" + none_to_str(self.weapon_l_3_range) + \
                   "/ダイスコスト:" + none_to_str(self.weapon_l_3_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.weapon_l_3_cost_bullets) + \
                   "/属性:" + none_to_str(self.weapon_l_3_element) + \
                   "/火力タイプ:" + none_to_str(self.weapon_l_3_attacktype) + \
                   "/Hit数:" + none_to_str(self.weapon_l_3_hitnum) + \
                   "/威力:" + none_to_str(self.weapon_l_3_attack)

        text = text + "\n[*]肩武装R:" + none_to_str(self.shoulder_r_name) + \
               "\nカテゴリー:" + none_to_str(self.shoulder_r_category) + \
               "/威力補正:" + none_to_str(self.shoulder_r_mod) + \
               "/弾数:" + none_to_str(self.shoulder_r_oneline_point) + \
               "×" + none_to_str(self.shoulder_r_line_num) + "Line"

        if not none_to_str(self.shoulder_r_1_range) == "":
            text = text + "\n①レンジ:" + none_to_str(self.shoulder_r_1_range) + \
                   "/ダイスコスト:" + none_to_str(self.shoulder_r_1_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.shoulder_r_1_cost_bullets) + \
                   "/属性:" + none_to_str(self.shoulder_r_1_element) + \
                   "/火力タイプ:" + none_to_str(self.shoulder_r_1_attacktype) + \
                   "/Hit数:" + none_to_str(self.shoulder_r_1_hitnum) + \
                   "/威力:" + none_to_str(self.shoulder_r_1_attack)

        if not none_to_str(self.shoulder_r_2_range) == "":
            text = text + "\n②レンジ:" + none_to_str(self.shoulder_r_2_range) + \
                   "/ダイスコスト:" + none_to_str(self.shoulder_r_2_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.shoulder_r_2_cost_bullets) + \
                   "/属性:" + none_to_str(self.shoulder_r_2_element) + \
                   "/火力タイプ:" + none_to_str(self.shoulder_r_2_attacktype) + \
                   "/Hit数:" + none_to_str(self.shoulder_r_2_hitnum) + \
                   "/威力:" + none_to_str(self.shoulder_r_2_attack)

        if not none_to_str(self.shoulder_r_3_range) == "":
            text = text + "\n③レンジ:" + none_to_str(self.shoulder_r_3_range) + \
                   "/ダイスコスト:" + none_to_str(self.shoulder_r_3_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.shoulder_r_3_cost_bullets) + \
                   "/属性:" + none_to_str(self.shoulder_r_3_element) + \
                   "/火力タイプ:" + none_to_str(self.shoulder_r_3_attacktype) + \
                   "/Hit数:" + none_to_str(self.shoulder_r_3_hitnum) + \
                   "/威力:" + none_to_str(self.shoulder_r_3_attack)

        text = text + "\n[*]肩武装L+:" + none_to_str(self.shoulder_l_name) + \
               "\nカテゴリー:" + none_to_str(self.shoulder_l_category) + \
               "/威力補正:" + none_to_str(self.shoulder_l_mod) + \
               "/弾数:" + none_to_str(self.shoulder_l_oneline_point) + \
               "×" + none_to_str(self.shoulder_l_line_num) + "Line"

        if not none_to_str(self.shoulder_l_1_range) == "":
            text = text + "\n①レンジ:" + none_to_str(self.shoulder_l_1_range) + \
                   "/ダイスコスト:" + none_to_str(self.shoulder_l_1_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.shoulder_l_1_cost_bullets) + \
                   "/属性:" + none_to_str(self.shoulder_l_1_element) + \
                   "/火力タイプ:" + none_to_str(self.shoulder_l_1_attacktype) + \
                   "/Hit数:" + none_to_str(self.shoulder_l_1_hitnum) + \
                   "/威力:" + none_to_str(self.shoulder_l_1_attack)

        if not none_to_str(self.shoulder_l_2_range) == "":
            text = text + "\n②レンジ:" + none_to_str(self.shoulder_l_2_range) + \
                   "/ダイスコスト:" + none_to_str(self.shoulder_l_2_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.shoulder_l_2_cost_bullets) + \
                   "/属性:" + none_to_str(self.shoulder_l_2_element) + \
                   "/火力タイプ:" + none_to_str(self.shoulder_l_2_attacktype) + \
                   "/Hit数:" + none_to_str(self.shoulder_l_2_hitnum) + \
                   "/威力:" + none_to_str(self.shoulder_l_2_attack)

        if not none_to_str(self.shoulder_l_3_range) == "":
            text = text + "\n③レンジ:" + none_to_str(self.shoulder_l_3_range) + \
                   "/ダイスコスト:" + none_to_str(self.shoulder_l_3_cost_dice) + \
                   "/弾数コスト:" + none_to_str(self.shoulder_l_3_cost_bullets) + \
                   "/属性:" + none_to_str(self.shoulder_l_3_element) + \
                   "/火力タイプ:" + none_to_str(self.shoulder_l_3_attacktype) + \
                   "/Hit数:" + none_to_str(self.shoulder_l_3_hitnum) + \
                   "/威力:" + none_to_str(self.shoulder_l_3_attack)

        defense_bullet_text = 0
        if self.defense_bullet == "":
            self.defense_bullet = 0
        else:
            defense_bullet_text = self.defense_bullet

        defense_explosion_text = 0
        if self.defense_explosion == "":
            self.defense_explosion = 0
        else:
            defense_explosion_text = self.defense_explosion

        defense_energy_text = 0
        if self.defense_energy == "":
            self.defense_energy = 0
        else:
            defense_energy_text = self.defense_energy

        text = text + "\n【防御性能】対弾:" + none_to_str(defense_bullet_text) + \
                "/対爆:" + none_to_str(defense_explosion_text) + \
                "/対EN:" + none_to_str(defense_energy_text)

        if "<pawntext_start>\n" in self.base_memo:
            after_start = self.base_memo.split("<pawntext_start>\n")[1]
            before_end = after_start.split("\n<pawntext_end>")[0]
            if "<no_default_pawntext>" in self.base_memo:
                text = before_end
            else:
                text = text + "\n\n" + before_end

        print(text)

        file_name = self.ac_name.replace("/", "_").replace("\"", "”") + "_ACテキストデータ.txt"

        f = open(file_name, 'w', encoding="utf-8")
        f.write(text)
        f.close()

        print("ACテキストデータを生成しました")
        self.output_pawn(text)

    def output_pawn(self, text_data):
        # 駒のココフォリア用データを出力する
        jsontext = {}
        jsontext["kind"] = "character"
        jsontext["data"] = {}
        jsontext["data"]["name"] = self.ac_name
        jsontext["data"]["memo"] = text_data
        jsontext["data"]["initiative"] = 0
        jsontext["data"]["status"] = []

        i = 0

        if self.core_line_num.isdecimal():
            for core in range(int(self.core_line_num)):
                corenum = core + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "CORE_" + none_to_str(corenum)
                jsontext["data"]["status"][i]["value"] = int(int(self.core_oneline_point))
                jsontext["data"]["status"][i]["max"] = int(int(self.core_oneline_point))
                i = i + 1

        if self.arms_line_num.isdecimal():
            for arms in range(int(self.arms_line_num)):
                armsnum = arms + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "ARM(R)_" + none_to_str(armsnum)
                jsontext["data"]["status"][i]["value"] = int(int(self.arms_oneline_point))
                jsontext["data"]["status"][i]["max"] = int(int(self.arms_oneline_point))
                i = i + 1

            for arms in range(int(self.arms_line_num)):
                armsnum = arms + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "ARM(L)_" + none_to_str(armsnum)
                jsontext["data"]["status"][i]["value"] = int(int(self.arms_oneline_point))
                jsontext["data"]["status"][i]["max"] = int(int(self.arms_oneline_point))
                i = i + 1

        if self.legs_line_num.isdecimal():
            for legs in range(int(self.legs_line_num)):
                legsnum = legs + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "LEGS_" + none_to_str(legsnum)
                jsontext["data"]["status"][i]["value"] = int(int(self.legs_oneline_point))
                jsontext["data"]["status"][i]["max"] = int(int(self.legs_oneline_point))
                i = i + 1

        if self.weapon_r_line_num.isdecimal():
            for weapon_r in range(int(self.weapon_r_line_num)):
                weapon_rnum = weapon_r + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "WEAPON_R_" + none_to_str(weapon_rnum)
                jsontext["data"]["status"][i]["value"] = int(self.weapon_r_oneline_point)
                jsontext["data"]["status"][i]["max"] = int(self.weapon_r_oneline_point)
                i = i + 1

        if self.weapon_l_line_num.isdecimal():
            for weapon_l in range(int(self.weapon_l_line_num)):
                weapon_lnum = weapon_l + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "WEAPON_L_" + none_to_str(weapon_lnum)
                jsontext["data"]["status"][i]["value"] = int(self.weapon_l_oneline_point)
                jsontext["data"]["status"][i]["max"] = int(self.weapon_l_oneline_point)
                i = i + 1

        if self.shoulder_r_line_num.isdecimal():
            for shoulder_r in range(int(self.shoulder_r_line_num)):
                shoulder_rnum = shoulder_r + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "SHOULDER_R_" + none_to_str(shoulder_rnum)
                jsontext["data"]["status"][i]["value"] = int(self.shoulder_r_oneline_point)
                jsontext["data"]["status"][i]["max"] = int(self.shoulder_r_oneline_point)
                i = i + 1

        if self.shoulder_l_line_num.isdecimal():
            for shoulder_l in range(int(self.shoulder_l_line_num)):
                shoulder_lnum = shoulder_l + 1
                jsontext["data"]["status"].append({})
                jsontext["data"]["status"][i]["label"] = "SHOULDER_L_" + none_to_str(shoulder_lnum)
                jsontext["data"]["status"][i]["value"] = int(self.shoulder_l_oneline_point)
                jsontext["data"]["status"][i]["max"] = int(self.shoulder_l_oneline_point)
                i = i + 1

        for dice in range(int(self.en_dice_max)):
            dicenum = dice + 1
            jsontext["data"]["status"].append({})
            jsontext["data"]["status"][i]["label"] = "EN_DICE_" + none_to_str(dicenum)
            jsontext["data"]["status"][i]["value"] = 0
            jsontext["data"]["status"][i]["max"] = 6
            i = i + 1

        status_i = i

        jsontext["data"]["params"] = []

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][0]["label"] = "ENダイス最大値"
        jsontext["data"]["params"][0]["value"] = none_to_str(self.en_dice_max.replace("　", "").replace(" ", ""))

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][1]["label"] = "ターン開始時ENダイス"
        jsontext["data"]["params"][1]["value"] = none_to_str(self.en_dice_turnstart.replace("　", "").replace(" ", ""))

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][2]["label"] = "手番開始時ENダイス"
        jsontext["data"]["params"][2]["value"] = none_to_str(self.en_dice_playerstart.replace("　", "").replace(" ", ""))

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][3]["label"] = "移動コスト"
        jsontext["data"]["params"][3]["value"] = none_to_str(self.move_cost.replace("　", "").replace(" ", ""))

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][4]["label"] = "回避コスト"
        jsontext["data"]["params"][4]["value"] = none_to_str(self.dodge_cost.replace("　", "").replace(" ", ""))

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][5]["label"] = "対システム障害"
        jsontext["data"]["params"][5]["value"] = none_to_str(self.incident)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][6]["label"] = "サーチ"
        jsontext["data"]["params"][6]["value"] = none_to_str(self.search)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][7]["label"] = "ハッキング"
        jsontext["data"]["params"][7]["value"] = none_to_str(self.hacking)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][8]["label"] = "マニューバ"
        jsontext["data"]["params"][8]["value"] = none_to_str(self.maneuver)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][9]["label"] = "対弾"
        jsontext["data"]["params"][9]["value"] = none_to_str(self.defense_bullet)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][10]["label"] = "対爆"
        jsontext["data"]["params"][10]["value"] = none_to_str(self.defense_explosion)

        jsontext["data"]["params"].append({})
        jsontext["data"]["params"][11]["label"] = "対EN"
        jsontext["data"]["params"][11]["value"] = none_to_str(self.defense_energy)
        j = 12

        jsontext["data"]["active"] = "true"
        jsontext["data"]["secret"] = "false"
        jsontext["data"]["invisible"] = "false"
        jsontext["data"]["hideStatus"] = "false"
        command = "//判定\n" + \
                                       "2D6+{対システム障害}+0 対システム障害判定\n" + \
                                       "2D6+{サーチ}+0 サーチ判定\n" + \
                                       "2D6+{ハッキング}+0 ハッキング判定\n" + \
                                       "2D6+{マニューバ}+0 マニューバ判定\n" + \
                                       "//ENダイス\n" + \
                                       "{ターン開始時ENダイス}B6 ターン開始時EN\n" + \
                                       "{手番開始時ENダイス}B6 手番開始時EN\n" + \
                                       "//部位決定\n" + \
                                       "1D6 部位決定\n" + \
                                       "choice(CORE,CORE,ARM(R),ARM(L),LEGS,LEGS) 部位決定\n" + \
                                       "//攻撃"

        if not none_to_str(self.weapon_r_1_attack) == "":
            weapon_r_1_command = "\n" + self.weapon_r_name + \
                                 "/①レンジ:" + none_to_str(self.weapon_r_1_range) + \
                                 "/ダイスコスト:" + none_to_str(self.weapon_r_1_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.weapon_r_1_cost_bullets) + \
                                 "/属性:" + none_to_str(self.weapon_r_1_element) + \
                                 "/火力タイプ:" + none_to_str(self.weapon_r_1_attacktype) + \
                                 "/Hit数:" + none_to_str(self.weapon_r_1_hitnum) + \
                                 "/威力:" + none_to_str(self.weapon_r_1_attack)

            command = command + weapon_r_1_command

        if not none_to_str(self.weapon_r_2_attack) == "":
            weapon_r_2_command = "\n" + self.weapon_r_name + \
                                 "/②レンジ:" + none_to_str(self.weapon_r_2_range) + \
                                 "/ダイスコスト:" + none_to_str(self.weapon_r_2_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.weapon_r_2_cost_bullets) + \
                                 "/属性:" + none_to_str(self.weapon_r_2_element) + \
                                 "/火力タイプ:" + none_to_str(self.weapon_r_2_attacktype) + \
                                 "/Hit数:" + none_to_str(self.weapon_r_2_hitnum) + \
                                 "/威力:" + none_to_str(self.weapon_r_2_attack)

            command = command + weapon_r_2_command

        if not none_to_str(self.weapon_r_3_attack) == "":
            weapon_r_3_command = "\n" + self.weapon_r_name + \
                                 "/③レンジ:" + none_to_str(self.weapon_r_3_range) + \
                                 "/ダイスコスト:" + none_to_str(self.weapon_r_3_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.weapon_r_3_cost_bullets) + \
                                 "/属性:" + none_to_str(self.weapon_r_3_element) + \
                                 "/火力タイプ:" + none_to_str(self.weapon_r_3_attacktype) + \
                                 "/Hit数:" + none_to_str(self.weapon_r_3_hitnum) + \
                                 "/威力:" + none_to_str(self.weapon_r_3_attack)

            command = command + weapon_r_3_command

        if not none_to_str(self.weapon_l_1_attack) == "":
            weapon_l_1_command = "\n" + self.weapon_l_name + \
                                 "/①レンジ:" + none_to_str(self.weapon_l_1_range) + \
                                 "/ダイスコスト:" + none_to_str(self.weapon_l_1_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.weapon_l_1_cost_bullets) + \
                                 "/属性:" + none_to_str(self.weapon_l_1_element) + \
                                 "/火力タイプ:" + none_to_str(self.weapon_l_1_attacktype) + \
                                 "/Hit数:" + none_to_str(self.weapon_l_1_hitnum) + \
                                 "/威力:" + none_to_str(self.weapon_l_1_attack)

            command = command + weapon_l_1_command

        if not none_to_str(self.weapon_l_2_attack) == "":
            weapon_l_2_command = "\n" + self.weapon_l_name + \
                                 "/②レンジ:" + none_to_str(self.weapon_l_2_range) + \
                                 "/ダイスコスト:" + none_to_str(self.weapon_l_2_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.weapon_l_2_cost_bullets) + \
                                 "/属性:" + none_to_str(self.weapon_l_2_element) + \
                                 "/火力タイプ:" + none_to_str(self.weapon_l_2_attacktype) + \
                                 "/Hit数:" + none_to_str(self.weapon_l_2_hitnum) + \
                                 "/威力:" + none_to_str(self.weapon_l_2_attack)

            command = command + weapon_l_2_command

        if not none_to_str(self.weapon_l_3_attack) == "":
            weapon_l_3_command = "\n" + self.weapon_l_name + \
                                 "/③レンジ:" + none_to_str(self.weapon_l_3_range) + \
                                 "/ダイスコスト:" + none_to_str(self.weapon_l_3_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.weapon_l_3_cost_bullets) + \
                                 "/属性:" + none_to_str(self.weapon_l_3_element) + \
                                 "/火力タイプ:" + none_to_str(self.weapon_l_3_attacktype) + \
                                 "/Hit数:" + none_to_str(self.weapon_l_3_hitnum) + \
                                 "/威力:" + none_to_str(self.weapon_l_3_attack)

            command = command + weapon_l_3_command

        if not none_to_str(self.shoulder_r_1_attack) == "":
            shoulder_r_1_command = "\n" + self.shoulder_r_name + \
                                 "/①レンジ:" + none_to_str(self.shoulder_r_1_range) + \
                                 "/ダイスコスト:" + none_to_str(self.shoulder_r_1_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.shoulder_r_1_cost_bullets) + \
                                 "/属性:" + none_to_str(self.shoulder_r_1_element) + \
                                 "/火力タイプ:" + none_to_str(self.shoulder_r_1_attacktype) + \
                                 "/Hit数:" + none_to_str(self.shoulder_r_1_hitnum) + \
                                 "/威力:" + none_to_str(self.shoulder_r_1_attack)

            command = command + shoulder_r_1_command

        if not none_to_str(self.shoulder_r_2_attack) == "":
            shoulder_r_2_command = "\n" + self.shoulder_r_name + \
                                 "/②レンジ:" + none_to_str(self.shoulder_r_2_range) + \
                                 "/ダイスコスト:" + none_to_str(self.shoulder_r_2_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.shoulder_r_2_cost_bullets) + \
                                 "/属性:" + none_to_str(self.shoulder_r_2_element) + \
                                 "/火力タイプ:" + none_to_str(self.shoulder_r_2_attacktype) + \
                                 "/Hit数:" + none_to_str(self.shoulder_r_2_hitnum) + \
                                 "/威力:" + none_to_str(self.shoulder_r_2_attack)

            command = command + shoulder_r_2_command

        if not none_to_str(self.shoulder_r_3_attack) == "":
            shoulder_r_3_command = "\n" + self.shoulder_r_name + \
                                 "/③レンジ:" + none_to_str(self.shoulder_r_3_range) + \
                                 "/ダイスコスト:" + none_to_str(self.shoulder_r_3_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.shoulder_r_3_cost_bullets) + \
                                 "/属性:" + none_to_str(self.shoulder_r_3_element) + \
                                 "/火力タイプ:" + none_to_str(self.shoulder_r_3_attacktype) + \
                                 "/Hit数:" + none_to_str(self.shoulder_r_3_hitnum) + \
                                 "/威力:" + none_to_str(self.shoulder_r_3_attack)

            command = command + shoulder_r_3_command

        if not none_to_str(self.shoulder_l_1_attack) == "":
            shoulder_l_1_command = "\n" + self.shoulder_l_name + \
                                 "/①レンジ:" + none_to_str(self.shoulder_l_1_range) + \
                                 "/ダイスコスト:" + none_to_str(self.shoulder_l_1_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.shoulder_l_1_cost_bullets) + \
                                 "/属性:" + none_to_str(self.shoulder_l_1_element) + \
                                 "/火力タイプ:" + none_to_str(self.shoulder_l_1_attacktype) + \
                                 "/Hit数:" + none_to_str(self.shoulder_l_1_hitnum) + \
                                 "/威力:" + none_to_str(self.shoulder_l_1_attack)

            command = command + shoulder_l_1_command

        if not none_to_str(self.shoulder_l_2_attack) == "":
            shoulder_l_2_command = "\n" + self.shoulder_l_name + \
                                 "/②レンジ:" + none_to_str(self.shoulder_l_2_range) + \
                                 "/ダイスコスト:" + none_to_str(self.shoulder_l_2_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.shoulder_l_2_cost_bullets) + \
                                 "/属性:" + none_to_str(self.shoulder_l_2_element) + \
                                 "/火力タイプ:" + none_to_str(self.shoulder_l_2_attacktype) + \
                                 "/Hit数:" + none_to_str(self.shoulder_l_2_hitnum) + \
                                 "/威力:" + none_to_str(self.shoulder_l_2_attack)

            command = command + shoulder_l_2_command

        if not none_to_str(self.shoulder_l_3_attack) == "":
            shoulder_l_3_command = "\n" + self.shoulder_l_name + \
                                 "/③レンジ:" + none_to_str(self.shoulder_l_3_range) + \
                                 "/ダイスコスト:" + none_to_str(self.shoulder_l_3_cost_dice) + \
                                 "/弾数コスト:" + none_to_str(self.shoulder_l_3_cost_bullets) + \
                                 "/属性:" + none_to_str(self.shoulder_l_3_element) + \
                                 "/火力タイプ:" + none_to_str(self.shoulder_l_3_attacktype) + \
                                 "/Hit数:" + none_to_str(self.shoulder_l_3_hitnum) + \
                                 "/威力:" + none_to_str(self.shoulder_l_3_attack)

            command = command + shoulder_l_3_command

        command = command + "\n//特技"

        if not none_to_str(self.weapon_r_skill) == "":
            command = command + "\n" +self.weapon_r_skill.replace("\n", "")

        if not none_to_str(self.weapon_l_skill) == "":
            command = command + "\n" +self.weapon_l_skill.replace("\n", "")

        if not none_to_str(self.shoulder_r_skill) == "":
            command = command + "\n" +self.shoulder_r_skill.replace("\n", "")

        if not none_to_str(self.shoulder_l_skill) == "":
            command = command + "\n" +self.shoulder_l_skill.replace("\n", "")

        for i in range(len(self.skill_effect)):
            if not self.skill_effect[i] == "":
                command = command + "\n特技名:" + self.skill_name[i] + \
                          "/種別:" + self.skill_type[i] + "/タイミング:" + \
                          self.skill_timing[i] + \
                          "/代償:" + self.skill_cost[i] + "/効果:" + self.skill_effect[i].replace("\n", "")

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
        file_name = self.ac_name.replace("/", "_").replace("\"", "”") + "_AC駒データ.txt"

        with open(file_name, 'w', encoding="utf-8") as filedata:  # 第二引数：writableオプションを指定
            json.dump(jsontext, filedata, ensure_ascii=False)

        print("AC駒データを生成しました")


def get_data(value):
    print("URL=" + value)
    url = value
    driver = webdriver.Chrome()
    driver.get(url)
    ac = ArmoredCoreData()
    time.sleep(5)

    ac.input_data(driver, url)
    ac.output_text()

    driver.quit()

    tkinter.messagebox.showinfo(title="完了", message="駒データを生成しました")

    sys.exit()


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title(u"TRPG ARMORED CORE VI FIRES OF RUBICON ココフォリア用駒データ作成ツール")
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
    Static1 = tkinter.Label(frame1, text=u'キャラクターシートURL\nhttps://character-sheets.appspot.com/ac6/')
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