'''
题目: 输入一个正整数，按照从小到大的顺序输出它的所有质因子
'''
'''
例子: 180 = 2 * 2 * 3 * 3 * 5, 所有的数都是质数（质数: 除了 1 和 本身，不能被其他数整除）
'''

def ZYZ(num):
    for item in range(2, num+1):
        while num % item == 0:
            print(item)
            # 更新 num
            num = num / item

ZYZ(180)