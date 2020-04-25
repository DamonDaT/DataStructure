'''
【递归】 题目: 给定一个字符串，按字典序输出其所有不重复的全排列
例子: 输入'ABC'，输出{'ACB', 'CBA', 'ABC', 'BAC', 'CAB', 'BCA'}
'''
'''
思路: 递归，每次固定一个元素，对其他元素进行求解
'''

# 字符串形式
def permutation_str(ss):
    # 递归终止条件
    if len(ss) <= 1:
        return ss
    # 集合去重
    res = set()
    # 遍历字符串，每次固定一个元素
    for i in range(len(ss)):
        # 在固定一个字符串的前提下，其他元素进行全排列
        for j in permutation_str(ss[:i] + ss[i+1:]):
            # 添加元素并去重
            res.add(ss[i] + j)
    # 返回已排列的结果
    return sorted(res)

print(permutation_str('ABC'))


# 数组形式
def permutation_list(nums):
    # 递归终止条件
    if nums is None: return []
    if len(nums) == 1: return [nums]
    # 数组
    res = []
    for x in nums:
        ys = nums + []
        # 移除元素
        ys.remove(x)
        # 遍历数组，每次固定一个元素
        for y in permutation_list(ys):
            # 去重
            if [x]+y not in res:
                res.append([x]+y)
    # 返回已排列的结果
    return sorted(res)

print(permutation_list([1,2,3]))