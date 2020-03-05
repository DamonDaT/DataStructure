'''
题目: 判断 101-200 之间有多少个素数，并输出所有素数
'''
'''
素数: 用一个数分别去除 2 到 sqrt(这个数)，如果能被整除， 则表明该数不是素数，反之则是素数
'''

from math import sqrt

total = 0 # 存储素数的个数
leap = 1 # 用于判断是否为素数的标记，leap == 1 表示为素数， leap == 0 表示不是素数

for num in range(101, 201):
   k = int(sqrt(num+1))
   for i in range(2, k+1):
      if num % i == 0:
         leap = 0
         break
   if leap == 1:
      print("%d" % num, end=" ")
      total += 1
      if total % 10 == 0:
         print(" ")
   leap = 1 # 重置 leap 值

print("The total is %d" % total)