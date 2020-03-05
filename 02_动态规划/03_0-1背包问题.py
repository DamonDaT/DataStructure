'''
【动态规划】 题目: 给定一些物品和一个背包，物品的大小存在 w 数组里，价值存在 v 数组里
背包的大小为 C，求放入放入背包的物品的总价值最高是多少
'''
'''
思路: 
遍历一遍放入所有物品的可能性，从 1 到 len(w), range(1, len(w)+1)
在上述每次遍历下，遍历一遍所有的背包大小的可能性，从 1 到 C, range(1, C+1)
此时去判断背包是否还有空间，要么放下一个物品，要么不放
'''

import numpy as np

def knapsack(w, v, C):
    mem = np.zeros((len(w)+1, C+1))
    for i in range(1, len(w)+1):
        for j in range(1, C+1):
            if w[i-1] <= j: # 如果还有空间,要么选下一个放，要么不放
                mem[i,j] = max(mem[i,j], mem[i-1,j], mem[i-1,j-w[i-1]]+v[i-1])
            else:
                mem[i,j] = mem[i-1,j]

    return mem

print(knapsack([4,6,2,2,5,1], [8,10,6,3,7,2], 12))