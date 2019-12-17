import numpy as np
from GameKOF.Kungfu.Ability import *
from GameKOF.Kungfu.Skill import *
from GameKOF.Cards.Card import *

##计算默认出1,1+2,1+2+3
def normalTakeOut(list):
    return [list[0], list[0]+list[1], list[0]+list[1]+list[2]]

class Hero:
    def __init__(self, hp, three_cards:handCard):
        self.hp = hp
        self.hand_card = three_cards

    ##结算被动
    def ability_effect(self):
        if (self.ability is not None):
            for i in range(len(self.ability)):
                self.ability[i].effect(self.hand_card)

    ##出牌,要结合技能方法定义，默认按照威力大优先出牌，出牌结果为一个包含6个数值的二维数组[[伤害],[招架]]，例：[[4,5,6],[0,3,6]]
    def takeoutCards(self):
        if (self.skill is not None):
            for i in range(len(self.skill)):
                self.skill[i].effect(self.hand_card)
        return [normalTakeOut(self.hand_card.damage_list), normalTakeOut(self.hand_card.defense_list)]

    ##承伤
    def getDamage(self, damage):
        self.hp -= damage

    ##回复
    def getHealth(self, health):
        self.hp += health

    ##立即死亡
    def getZero(self):
        self.hp = 0

##白板
class XiaoBai(Hero):
    def __init__(self, hp, three_cards:handCard):
        self.hp = hp
        self.ability = None
        self.skill = None
        self.hand_card = three_cards

##剑圣
class SwordMaster(Hero):
    def __init__(self, hp, three_cards:handCard):
        self.hp = hp
        self.ability = [YuJianShu()]
        self.skill = [WanJianGuiZong()]
        self.hand_card = three_cards

