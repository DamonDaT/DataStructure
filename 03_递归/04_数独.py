'''
【递归】 题目: 写段程序，求解数独
'''
'''
【输入】 逐行输入
 5  3  0  0  7  0  0  0  0 
 6  0  0  1  9  5  0  0  0 
 0  9  0  0  0  0  0  6  0 
 8  0  0  0  6  0  0  0  3 
 0  0  0  8  0  3  0  0  1 
 0  0  0  0  2  0  0  0  6 
 0  6  0  0  0  0  2  8  0 
 0  0  0  4  1  9  0  0  5 
 0  0  0  0  8  0  0  7  9
'''
'''
【输出】
 5  3  4  2  7  6  9  1  8 
 6  2  8  1  9  5  3  4  7 
 1  9  7  3  4  8  5  6  2 
 8  1  5  9  6  4  7  2  3 
 2  7  6  8  5  3  4  9  1 
 3  4  9  7  2  1  8  5  6 
 9  6  1  5  3  7  2  8  4 
 7  8  2  4  1  9  6  3  5 
 4  5  3  6  8  2  1  7  9
'''


# 数据输入函数
def data_input():
    data = []
    for i in range(9):
        data_line = list(map(int, input('请输入第 {} 行: '.format(i + 1)).split()))
        data.append(data_line)
    print('你的数据:')
    print_data(data)  # 打印函数
    return data


# 打印数据函数
def print_data(data):
    for i in range(9):
        for j in range(9):
            # {:^3}，字符宽度为 3
            print('{:^3}'.format(data[i][j]), end='')
        print('')  # 换行


# data 为矩阵，(x, y)为数的坐标，第 y 行 and 第 x 列，num 为填充的数字
def judge(data, x, y, num):
    # 行
    if data[y].count(num) > 0:
        return False
    # 列
    for i in range(9):
        if data[i][x] == num:
            return False
    # 九宫格
    for i in range(3):
        for j in range(3):
            if data[i + 3 * (y // 3)][j + 3 * (x // 3)] == num:
                return False
    return True


# 建立 0 值列表，列表内容包括 0 值的 (x, y) 坐标 和 候选数字集合
def data_all_list(data):
    data_list = []
    for y in range(9):
        for x in range(9):
            if data[y][x] == 0:
                # 列表中有坐标信息以及备选的数字
                data_list.append([(x, y), [1, 2, 3, 4, 5, 6, 7, 8, 9]])
    return data_list


# 初始化 0 值列表，更新初始候选数字集合，其实可以和上一个函数写到同一个函数里
def data_avaliable_list(data, data_list, index):
    for blank_index in range(index, len(data_list)):
        data_list[blank_index][1] = []
        for num in range(1, 10):
            if judge(data, data_list[blank_index][0][0], data_list[blank_index][0][1], num):
                data_list[blank_index][1].append(num)
    return data_list


# 递归实现 对 0 值的位置进行填充
def set_num(data, data_list, index):
    if index < len(data_list):
        # 取单个数据
        single = data_list[index]
        # 遍历 单个数据 的 备选数据集
        for num in single[1]:
            if judge(data, single[0][0], single[0][1], num):
                # 填充值
                data[single[0][1]][single[0][0]] = num
                # 递归
                tem_data = set_num(data, data_list, index+1)
                # 当数字无法填充时会返回 None，这里要进行判断，当递归返回值非空时才传给上层
                if tem_data is not None:
                    return tem_data
        # 当 for 循环结束时依然执行这里，说明函数最后无返回值，数字无法继续填充，需要执行归零操作
        data[single[0][1]][single[0][0]] = 0
    else:
        return data


# 主函数
def main():
    try:
        data = data_input()
        data_list = data_avaliable_list(data, data_all_list(data), 0)
        newdata = set_num(data, data_list, 0)
        print('求解结果:')
        print_data(newdata)
    except:
        print('数独数据输入有误，请检查并重新输入，空白格请输入 0')


# 执行程序
main()
