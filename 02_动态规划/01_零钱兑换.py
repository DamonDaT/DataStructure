'''
【动态规划】 题目: 给定一组面值不同的硬币 coins，求凑够 n 的最少的硬币数
'''
'''
思路:
M(n) = M(n-c[i])，凑够（当前数值（n））的硬币的数量，
等于凑够（当前数值（n）减去 给的硬币的面值）的硬币的数量 + 1
'''

def coinChange(coins, amount):
    if amount  == 0:
        return 0
    if len(coins) == 0:
        return -1
    if len(coins) == 1 and coins[0] > amount:
        return -1
    mem = [0] + [-1] * amount # 建立存储空间并初始化为-1, 第一个是0
    for i in range(1, amount+1):
        cur_min = amount + 1
        for c in coins:
            if c <= i: # 当钱币面值小于当前需要凑的金额时
                cur_min = min(mem[i-c], cur_min)
        # cur_min 存储的是 凑够前一阶段面值的最少次数，然后基于这个数值 +1 即可
        mem[i] = cur_min + 1 if cur_min < amount + 1 else amount + 1
        print(mem)
    if mem[-1] == amount + 1:
        return -1
    else:
        return mem[-1]

print(coinChange([2,3], 7))