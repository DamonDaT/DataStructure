'''
【递归】 题目: N Queens，N 皇后问题，西洋象棋，如何将 n 个皇后放置在 n x n 的棋盘上，并且使得皇后之间不能相互攻击
'''

result = []

# 深度优先遍历
def DFS(cols, na, pie, n):
    '''
    :param cols: 列表，存储皇后所在的列的索引
    :param na: 列表，存储皇后辐射的反斜区域
    :param pie: 列表，存储皇后辐射的正斜区域
    :param n: 数字，表示有几个皇后
    '''
    p = len(cols)
    if p == n:
        result.append(cols)
        return None
    for q in range(n):
        if q not in cols and p-q not in na and p+q not in pie:
            DFS(cols+[q], na+[p-q], pie+[p+q], n)

# 调用函数并返回结果
def solveNQueen(n):
    DFS([], [], [], n)
    return [ ['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result ]

print(solveNQueen(4))