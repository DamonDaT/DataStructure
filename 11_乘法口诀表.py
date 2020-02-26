'''
题目: 输出 9*9 乘法口诀表
'''

for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%2d" % (j, i, i*j), end=" ")
    print(" ")

