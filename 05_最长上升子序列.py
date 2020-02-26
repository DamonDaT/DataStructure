'''
【动态规划】 题目: 给定一个数组，求该数组的最长上升子序列的个数
'''
'''
思路: 
遍历数组，在每次遍历的基础上，遍历从0到该位置的数组，时间复杂度为O(n^2)
'''

def lengthOfLIS(nums):
    if len(nums) <= 1:
        return len(nums)
    mem = [1] * len(nums)
    for j in range(1, len(nums)):
        for i in range(0, j):
            if nums[i] < nums[j]:
                mem[j] = max(mem[j], mem[i]+1)
    return mem

print(lengthOfLIS([1,2,3,4,0,2,3]))