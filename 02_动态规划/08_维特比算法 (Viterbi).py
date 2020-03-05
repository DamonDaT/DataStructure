'''
【动态规划】 题目: (词性标注) 给定一个字符串，判断里面每个单词的词性
'''
'''
思路: 维特比算法，寻找最有可能产生观测时间序列的隐含状态序列
结合贪心科技https://www.greedyai.com/course/55/task/2015/show
'''

import numpy as np
from math import log

# 将单词转换成数字的表现形式
word2id = {"word1":123, "word2":234} # ...
# 将数字转化成词性的表现形式
id2tag = {123:"pos", 234:"nn", 345:"vb"} # ...
# 所有词性的个数
N = len(["pos", "vb", "nn"]) # ...

# 维特比算法
def viterbi(x, pi, A, B):
    """
    :param x: 用户输入的数据，如 "I like playing soccer"
    :param pi: 初始化 tags(pos) 的概率
    :param A: 给定 tag，每个单词出现的概率
    :param B: tag 之间的转移概率
    """

    x = [word2id[word] for word in x.split()] # x:[4521, 412, 542, ...]
    T = len(x)

    dp = np.zeros((T, N)) # dp[i][j]: w1...wi，假设 wi 的 tag 是第 j 个 tag
    # ptr = np.zeros((T, N), dtype=int), 存储路径，即指针
    ptr = np.array([[0 for _ in range(N)] for _ in range(T)])

    # 不太懂这里吗，就是初始化第一行
    for j in range(N): # bacecase for DP 算法，计算第一行
        dp[0][j] = log(pi[j]) + log(A[j][x[0]])

    for i in range(1, T): # 每个单词
        for j in range(N): # 每个词性
            dp[i][j] = -9999999
            for k in range(N): # 从每一个 k 可以到达 j
                score = dp[i-1][k] + log(B[k][j]) + log(A[j][x[i]])
                if score > dp[i][j]:
                    dp[i][j] = score
                    ptr[i][j] = k

    # decoding: 把最好的 tag sequence 打印出来
    best_seq = [0]*T # best_seq = [1, 5, 2, 23,4, ...]
    # step1: 找出对应于最后一个单词的词性
    best_seq[T-1] = np.argmax(dp[T-1])

    # step2: 通过从后到前的循环来一次求出每个单词的词性
    for i in range(T-2, -1, -1): # T-2, T-1, ..., 1, 0
        best_seq[i] = ptr[i+1][best_seq[i+1]]

    # 到目前为止，best_seq 存放了对应于 x 的词性序列
    for i in range(len(best_seq)):
        print(id2tag[best_seq[i]])


