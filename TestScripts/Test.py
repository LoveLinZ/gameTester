import numpy
import matplotlib.pyplot as plt

quan = [4, 0]
zhang = [2, 2]
jiao = [2, 2]
zhi = [1, 3]
jian = [3, 1]
nei = [0, 4]

cardpool = [quan, zhang, jiao, zhi, jian, nei]*5
numpy.random.shuffle(cardpool)

takedamage = 0
getdamage = 0
takedamageCount = 0
getdamageCount = 0
count = 0
list_x = []
list_y1 = []
list_y2 = []
for j in range(1000):
    list_x.append(j)
    for i in range(5):
        value1 = cardpool[6 * i][0]
        value2 = cardpool[6 * i + 1][0]
        value3 = cardpool[6 * i + 2][0]
        value4 = cardpool[6 * i + 3][0]
        value5 = cardpool[6 * i + 4][0]
        value6 = cardpool[6 * i + 5][0]
        value7 = cardpool[6 * i][1]
        value8 = cardpool[6 * i + 1][1]
        value9 = cardpool[6 * i + 2][1]
        value10 = cardpool[6 * i + 3][1]
        value11 = cardpool[6 * i + 4][1]
        value12 = cardpool[6 * i + 5][1]
        if (value1 - value8) > 0:
            takedamage += (value1 - value8)
        if (value1 + value3 - value8 - value10) > 0:
            takedamage += (value1 + value3 - value8 - value10)
        if (value1 + value3 + value5 - value8 - value10 - value12) > 0:
            takedamage += (value1 + value3 + value5 - value8 - value10 - value12)
        if (value2 - value7) > 0:
            getdamage += (value2 - value7)
        if (value2 + value4 - value7 - value9) > 0:
            getdamage += (value2 + value4 - value7 - value9)
        if (value2 + value4 + value6 - value7 - value9 - value11) > 0:
            getdamage += (value2 + value4 + value6 - value7 - value9 - value11)
    takedamageCount += takedamage
    getdamageCount += getdamage
    list_y1.append(takedamage)
    list_y2.append(getdamage)
    numpy.random.shuffle(cardpool)
    takedamage = 0
    getdamage = 0

##plt.plot(list_x, list_y1, color='red', linewidth=2.0, linestyle='--')
plt.plot(list_x, list_y2, color='blue', linewidth=3.0, linestyle='-.')
plt.show()
print("平均伤害：%d" %(takedamageCount/1000))
print("平均承伤：%d" %(getdamageCount/1000))
