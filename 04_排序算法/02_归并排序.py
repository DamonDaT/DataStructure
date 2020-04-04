'''
题目: Python 实现归并排序
'''
'''
思路: 
1. 将数组分半
2. 对分半的数组进行比较和排序
3. 合并排序好的数组
'''

def merge_sort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    # 将列表分成更小的两个列表
    mid = len(seq) // 2
    # 分别对左右两个列表进行处理，分别返回两个排序好的列表
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    # 对排序好的两个列表合并，产生一个新的排序好的列表
    return merge(left, right)

def merge(left, right):
    """ 合并两个已排序好的列表，产生一个新的已排序好的列表 """
    result = []  # 新的已排序好的列表
    i = 0  # 下标
    j = 0
    # 对两个列表中的元素 两两对比。
    # 将最小的元素，放到 result 中，并对当前列表下标加 1
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

print(merge_sort([5,3,0,6,1,4]))