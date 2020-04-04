'''
【动态规划】 题目: 给定一个字符串，求该字符串的最长回文子串
'''
'''
思路: 如果 mem[i][j] 为回文，那么 mem[i+1][j-1] 也一定为回文
'''


def LPS(str):
    if len(str) <= 1:
        return str

    s = list(str)  # 数组
    l = len(str)  # 长度

    mem = [[0] * l for _ in range(l)]
    # 初始化 mem 数组
    for i in range(l):
        mem[i][i] = True
        # 当 k=2 时要用到, 不是太理解, 待补充
        mem[i][i - 1] = True

    left = 0  # 左索引
    right = 0  # 右索引

    for k in range(2, l + 1):
        for i in range(0, l - k + 1):
            j = i + k - 1
            if s[i] == s[j] and mem[i + 1][j - 1]:
                mem[i][j] = True
                if right - left + 1 < k:
                    left = i
                    right = j

    return str[left:right + 1]


print(LPS('iabcbaj'))