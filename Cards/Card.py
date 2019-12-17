from enum import Enum
import numpy as np

##计算默认出1,1+2,1+2+3
def normalTakeOut(list):
    return [list[0], list[0]+list[1], list[0]+list[1]+list[2]]

##拳、掌、脚、指、剑、内
class cardType(Enum):
    QUAN = 1
    ZHANG = 2
    JIAO = 3
    ZHI = 4
    JIAN = 5
    NEI = 6

class Card:
    def __init__(self, type, damage, defense):
        self.type = type
        self.damage = damage
        self.defense = defense

    ##单张牌面板伤害计算器
    def damageCalculator(self, card):
        takeDamage = 0
        getDamage = 0
        if (self.damage - card.defense) > 0:
            takeDamage = (self.damage - card.defense)
        if (card.damage - self.defense) > 0:
            getDamage = (card.damage - self.defense)
        return [takeDamage, getDamage]

    ##卡牌转变类型，类型数值都会变化
    def changeType(self, type):
        self.type = type
        if type == cardType.QUAN.value:
            self.damage = 4
            self.defense = 0
        if type == cardType.ZHANG.value:
            self.damage = 2
            self.defense = 2
        if type == cardType.JIAO.value:
            self.damage = 2
            self.defense = 2
        if type == cardType.ZHI.value:
            self.damage = 1
            self.defense = 3
        if type == cardType.JIAN.value:
            self.damage = 3
            self.defense = 1
        if type == cardType.NEI.value:
            self.damage = 0
            self.defense = 4

class Quan(Card):
    def __init__(self):
        self.type = cardType.QUAN.value
        self.damage = 4
        self.defense = 0

class Zhang(Card):
    def __init__(self):
        self.type = cardType.ZHANG.value
        self.damage = 2
        self.defense = 2

class Jiao(Card):
    def __init__(self):
        self.type = cardType.JIAO.value
        self.damage = 2
        self.defense = 2

class Zhi(Card):
    def __init__(self):
        self.type = cardType.ZHI.value
        self.damage = 1
        self.defense = 3

class Jian(Card):
    def __init__(self):
        self.type = cardType.JIAN.value
        self.damage = 3
        self.defense = 1

class Nei(Card):
    def __init__(self):
        self.type = cardType.NEI.value
        self.damage = 0
        self.defense = 4

##定义手牌，一次三张
class handCard:
    def __init__(self, card1:Card, card2:Card, card3:Card):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.damage_list = [self.card1.damage, self.card2.damage, self.card3.damage]
        self.defense_list = [self.card1.defense, self.card2.defense, self.card3.defense]
        self.damage_list.sort(reverse=True)
        self.defense_list.sort()


##手牌伤害计算器,三张手牌，参数为出牌后列表，参考函数takeoutCards,返回造成伤害和承伤总数
def handCardCalculate(hand_card1, hand_card2):
    take_damage = 0
    get_damage = 0
    if hand_card1[0][0] - hand_card2[1][0] > 0:
        take_damage += hand_card1[0][0] - hand_card2[1][0]
    if hand_card1[0][1] - hand_card2[1][1] > 0:
        take_damage += hand_card1[0][1] - hand_card2[1][1]
    if hand_card1[0][2] - hand_card2[1][2] > 0:
        take_damage += hand_card1[0][2] - hand_card2[1][2]
    if hand_card2[0][0] - hand_card1[1][0] > 0:
        get_damage += hand_card2[0][0] - hand_card1[1][0]
    if hand_card2[0][1] - hand_card1[1][1] > 0:
        get_damage += hand_card2[0][1] - hand_card1[1][1]
    if hand_card2[0][2] - hand_card1[1][2] > 0:
        get_damage += hand_card2[0][2] - hand_card1[1][2]
    return [take_damage, get_damage]

##定义牌库，共三十张
class cardPool:
    def __init__(self,cards:list):
        self.card_pool = cards

    ##洗牌
    def shuffle(self):
        np.random.shuffle(self.card_pool)

    ##分牌15+15
    def allocate(self):
        player1_cards = self.card_pool[:int(len(self.card_pool)/2)]
        player2_cards = self.card_pool[int(len(self.card_pool)/2):]
        return [player1_cards, player2_cards]
