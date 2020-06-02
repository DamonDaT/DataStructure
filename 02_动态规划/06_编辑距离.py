'''
【动态规划】 题目: 数组 A 变换成数组 B，提供 添加，删除，插入的操作，求最少的操作次数
'''
'''
思路: 
A[1,...,i] => B[1,...,j] : 
1. 添加: T(i-1, j) + 1 => T(i, j)
2. 删除: T(i, j-1) + 1 => T(i, j)
3. 替换: if A[i] == B[j]  T(i-1, j-1) => T(i, j) 
4. 替换: if A[i] ≠ B[j]   T(i-1, j-1) + 1 => T(i, j) 
'''

import numpy as np

def editDistance(word1, word2):
    if word1 == word2:
        return 0
    lenW1, lenW2 = len(word1), len(word2)
    # mem = [[0]*(lenW2+1) for _ in range(lenW1+1)]
    mem = np.zeros((lenW1+1, lenW2+1))
    for i in range(lenW1+1): mem[i][0] = i
    for j in range(lenW2+1): mem[0][j] = j
    for i in range(1, lenW1+1):
        for j in range(1, lenW2+1):
            # 如果当前字符相同, 不需要替换操作
            if word1[i-1] == word2[j-1]:
                # mem[i][j] = min(mem[i-1][j]+1, mem[i][j-1]+1, mem[i-1][j-1], mem[i-1][j-1]+1)
                # mem[i-1][j]+1: 删除操作
                # mem[i][j-1]+1: 添加操作
                # mem[i-1][j-1]: 无需替换操作
                mem[i][j] = min(mem[i-1][j]+1, mem[i][j-1]+1, mem[i-1][j-1])
            # 如果当前字符不同, 需要替换操作
            else:
                # mem[i-1][j]+1: 删除操作
                # mem[i][j-1]+1: 添加操作
                # mem[i-1][j-1]+1: 需要替换操作
                mem[i][j] = min(mem[i-1][j]+1, mem[i][j-1]+1, mem[i-1][j-1]+1)

    return mem[-1][-1]

print(editDistance("there", "thaerr"))