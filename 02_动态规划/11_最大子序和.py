'''
【动态规划】 题目: 给定一个数组，求该数组的最大子序和
'''
'''
思路: 
cur_max: 以第i个数字作为最后一个数字时，得到的最大子序和
last_max: 上一步最大的子序和
max_res: 存放结果
'''

def maxsubArray(nums):
    # 判断长度
    if len(nums) == 1:
        return nums[0]
    # max_res 存放最后的结果
    max_res = nums[0]
    # cur_max 存放到第i个数字的最大的值
    cur_max = last_max = nums[0]
    for i in range(1, len(nums)):
        # if else 语句确定 cur_max 的值
        if last_max + nums[i] < nums[i]:
            cur_max = nums[i]
        else:
            cur_max = last_max + nums[i]
        # 更新结果
        if cur_max > max_res:
            max_res = cur_max
        # 更新当前的最大子序和
        last_max = cur_max
    return max_res

print(maxsubArray([1,2,3,-1,4]))