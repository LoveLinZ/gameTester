from GameKOF.Cards.Card import *

class Ability:
    def __init__(self, name, describe):
        self.name = name
        self.describe = describe

##御剑术
class YuJianShu(Ability):
    def __init__(self):
        self.name = "御剑术"
        self.describe = "所有‘指’和‘内’视为‘剑’"

    def effect(self, three_cards:handCard):
        if three_cards.card1.type == 4 or three_cards.card1.type == 6:
            three_cards.card1.changeType(5)
        if three_cards.card2.type == 4 or three_cards.card2.type == 6:
            three_cards.card2.changeType(5)
        if three_cards.card3.type == 4 or three_cards.card3.type == 6:
            three_cards.card3.changeType(5)
        three_cards.damage_list = [three_cards.card1.damage, three_cards.card2.damage, three_cards.card3.damage]
        three_cards.defense_list = [three_cards.card1.defense, three_cards.card2.defense, three_cards.card3.defense]
        three_cards.damage_list.sort(reverse=True)
        three_cards.defense_list.sort()

