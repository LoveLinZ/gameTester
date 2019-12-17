from GameKOF.Cards.Card import *
from GameKOF.Kungfu.SkillPower import *

class Skill:
    def __init__(self, name, describe):
        self.name = name
        self.describe = describe

##万剑归宗
class WanJianGuiZong(Skill):
    def __init__(self):
        self.name = "万剑归宗"
        self.describe = "连招为‘剑剑剑’时，威力增加5"

    def effect(self, three_cards:handCard):
        if three_cards.card1.type == 5 and three_cards.card2.type == 5 and three_cards.card3.type == 5:
            three_cards.damage_list[2] += skillType.WanJianGuiZong.value


