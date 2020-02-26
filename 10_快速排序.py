'''
题目: Python 实现快速排序
'''
'''
思路: 
1. 以当前子序列的第一个值作为判定值
2. 两个指针 j 和 i 分别从后往前，从前完后扫描子序列
3. j 从后往前，把 小于 判定值的数值放到 i 位置
4. i 从前往后，把 大于 判定值的数值放到 j 位置
5. i 和 j 相遇的位置为空，将判定值放进此处
6. 二分循环，即拆分子序列，直到子序列个数为 1
'''

def quick_sort(nums, left, right):
    if left < right:
        i = left
        j = right
        # 取第一个元素为判定值
        pivot = nums[left]
        while i < j:

            # 交替扫描和交换
            # 从后往前找到第一个比判定值小的元素，交换位置
            while j > i and nums[j] > pivot:
                # 移动指针j
                j = j - 1
            if j > i:
                # 如果找到了，进行元素交换，并移动指针i
                nums[i] = nums[j]
                i = i + 1

            # 从前往后找到第一个比判定值大的元素，交换位置
            while i < j and nums[i] < pivot:
                # 移动指针i
                i = i + 1
            if i < j:
                nums[j] = nums[i]
                j = j - 1

        # 至此完成一趟快速排序，判定值的位置已经确定好了，就在i位置上（i和j)值相等
        nums[i] = pivot

        # 以 i 位置为起点，左后划分形成子序列
        quick_sort(nums, left, i-1)
        quick_sort(nums, i+1, right)

    return nums

print(quick_sort([1,5,2,3,9,0], 0, 5))