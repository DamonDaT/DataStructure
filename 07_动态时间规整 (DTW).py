'''
【动态规划】 任意不等长序列之间的距离计算, 比如可以用来做语音识别、股票相似K线的计算
'''
'''
1. 起始点与终止点： 一般起始点采用(0,0), 终止点采用 (len(s), len(t))
2. Local continuity:  在局部上做alignment的时候可以稍微灵活一些，比如跳过1个value等
3. Global Continuity:  从全局的角度设定的限制条件
4. 另外就是每一个路径的权重
'''
'''
参考链接: https://www.greedyai.com/course/55/task/2448/show#
'''

import numpy as np
import sys


# 定义距离
def euc_dist(v1, v2):
    return np.abs(v1 - v2)


# DTW 的核心过程，实现动态规划
def dtw(s, t):
    """
    s: source sequence
    t: target sequence
    """
    m, n = len(s), len(t)
    dtw = np.zeros((m, n))
    dtw.fill(sys.maxsize)

    # 初始化过程
    dtw[0, 0] = euc_dist(s[0], t[0])
    for i in range(1, m):
        dtw[i, 0] = dtw[i - 1, 0] + euc_dist(s[i], t[0])
    for i in range(1, n):
        dtw[0, i] = dtw[0, i - 1] + euc_dist(s[0], t[i])

    # 核心动态规划流程，此动态规划的过程依赖于上面的图
    for i in range(1, m):
        for j in range(max(1, i - 10), min(n, i + 10)):
            cost = euc_dist(s[i], t[j])
            ds = []
            ds.append(cost + dtw[i - 1, j])
            ds.append(cost + dtw[i, j - 1])
            ds.append(2 * cost + dtw[i - 1, j - 1])
            ds.append(3 * cost + dtw[i - 1, j - 2] if j > 1 else sys.maxsize)
            ds.append(3 * cost + dtw[i - 2, j - 1] if i > 2 else sys.maxsize)

            dtw[i, j] = min(ds)

    return dtw[m - 1, n - 1]


print(dtw([5, 6, 9], [5, 6, 7]))