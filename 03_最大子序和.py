def maxsubArray(nums):
    if len(nums) == 1:
        return nums[0]
    max_ret = nums[0]
    cur_max = last_max = nums[0]
    for i in range(1, len(nums)):
        if last_max + nums[i] < nums[i]:
            cur_max = nums[i]
        else:
            cur_max = last_max + nums[i]
        if cur_max > max_ret:
            max_ret = cur_max
        last_max = cur_max
    return max_ret

print(maxsubArray([-1,2,-1,-3,-4]))