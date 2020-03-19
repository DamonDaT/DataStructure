'''
【递归】 题目: 给定 length (表示组合的长度), cat (表示元素种类), 输出不重复组合的个数 (顺序不同都视为同一个)
例子: length = 2 (长度为2), cat = 3 (A,B,C), 结果为 6 (AA, AB, AC, BB, BC, CC)
'''
'''
思路: 递归，从子问题开始考虑，慢慢摸索递归的精髓
'''

# res 存储结果
res = 0

# 不同组合
def dfs(start, length, cat):
    global res
    if length == 0:
        res = (res + 1) % 1000000007
        return
    for i in range(start, cat+1):
        dfs(i, length-1, cat)

# 将不同组合的结果合在一起
def combine(length, cat):
    global res
    dfs(1, length, cat)
    return res

# 测试结果
length, cat = 9, 3
print(combine(length, cat))