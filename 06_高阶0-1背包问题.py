'''
【动态规划】 题目: 0-1背包问题的升级版
① 添加了主件和附件(0 表示主件，1 表示附件)，附件购买的同时，其对应的主件也必须购买
② 添加了主件的重要程度，用数值表示，需要最大化其价值（价格*重要程度）
'''
'''
思路: 
遍历一遍放入所有物品的可能性，从 1 到 allGoods (商品的数量)
在上述每次遍历下，遍历一遍所有的钱，从 1 到 allMoney
判断当前商品是否为主件，或者附件，分别处理
此时去判断剩余的钱是否还有空间，要么放下一个物品，要么不放
'''

import numpy as np

def getMaxValue(val, price, belong, allGoods, allMoney):
    '''
    :param val: 价值
    :param price: 价格
    :param belong: 附件的从属关系
    :param allGoods: 商品的数量
    :param allMoney: 总共拥有多少钱
    '''
    mem = np.zeros((allGoods+1, allMoney+1))

    # 遍历商品
    for i in range(1, allGoods+1):
        # 遍历总共的钱
        for j in range(1, allMoney+1):

            # 当前商品为主件
            if belong[i-1] == 0:
                if price[i-1] <= j:
                    # 要么不放，要么放
                    mem[i,j] = max(mem[i-1,j], mem[i-1,j-price[i-1]] + val[i-1])
                else:
                    # 不放
                    mem[i,j] = mem[i-1,j]

            # 当前商品为附件
            else:
                if price[i-1] + price[belong[i-1]] <= j:
                    # 要么放，要么不放
                    mem[i,j] = max(mem[i-1,j], mem[i-1,j-price[i-1]] + val[i-1])
                else:
                    # 不放
                    mem[i,j] = mem[i-1,j]

    return mem


print(getMaxValue([1600, 2000, 1500, 1200, 1000],
                  [800, 400, 300, 400, 500],
                  [0, 1, 1, 0, 0],
                  5, 1000))
