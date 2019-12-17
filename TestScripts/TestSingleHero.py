from GameKOF.Cards.Card import *
from GameKOF.Heros.Hero import *
from GameKOF.Heros.HeroHp import *
from GameKOF.Kungfu.Ability import *
from GameKOF.Kungfu.Skill import *
from GameKOF.Kungfu.SkillPower import *

def oneGame():
    ##拿出一副牌
    thirtyCards = [Quan(), Zhang(), Jiao(), Zhi(), Jian(), Nei()] * 5
    card_pool = cardPool(thirtyCards)

    ##洗牌
    card_pool.shuffle()

    ##30张牌分为15张自己的手牌和15张对方的手牌
    player1_handCards = card_pool.allocate()[0]
    player2_handCards = card_pool.allocate()[1]

    ##增加一个容器，存储结算数值
    result = [0, 0]

    ##测试英雄加入游戏，进行5次出牌
    for i in range(5):
        ##每次三张手牌并打出
        hero = SwordMaster(hpType.SwordMaster.value, handCard(player1_handCards[3 * i], player1_handCards[3 * i + 1],
                                                              player1_handCards[3 * i + 2]))
        ##被动
        hero.ability_effect()
        ##敌人手牌
        enemy = XiaoBai(hpType.XiaoBai.value,
                        handCard(player2_handCards[3 * i], player2_handCards[3 * i + 1], player2_handCards[3 * i + 2]))
        ##被动
        enemy.ability_effect()
        ##出牌
        hero_take_out = hero.takeoutCards()
        enemy_take_out = enemy.takeoutCards()
        ##结算一轮的伤害和承伤，针对player1
        result_one_turn = handCardCalculate(hero_take_out, enemy_take_out)
        result[0] += result_one_turn[0]
        result[1] += result_one_turn[1]
    return result

def main():
    take_damage = 0
    get_damage = 0
    for i in range(1000):
        take_damage += oneGame()[0]
        get_damage += oneGame()[1]
    print("平均伤害：%d" %(take_damage/5000))
    print("平均承伤：%d" %(get_damage/5000))

if __name__ == '__main__':
    main()
