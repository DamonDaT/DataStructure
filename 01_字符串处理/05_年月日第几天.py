'''
题目: 输入某年某月某日，判断这一天是这一年的第几天
'''

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

result_month = 0 # 定位到几月
result = 0 # 最终结果

months = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

if 0 < month <= 12:
    result_month = months[month - 1]
else:
    print('error')

result = result_month + day # 在不考虑是否为闰年的前提下，输出的结果

# 判断闰年的标准是: 能整除 4 且不能整除 100; 或者 能整除 400
leap = 0 # 用于存储闰年时，2月份多出的一天
if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
    leap = 1
if (leap == 1 and month >= 2):
    result += 1

print('It is the %dth day.' % result)