'''
题目: 生成编辑距离为1和2的单词
'''

def generate_edit_one(str):
    """
    给定一个字符串，生成编辑距离为 1 的字符串列表
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    # 将 str 拆分成前后两部分，如[("a", "pple"), ("ap", "ple"), ...]
    splits = [(str[:i], str[i:]) for i in range(len(str)+1)]
    # 插入操作
    inserts = [L + c + R for (L, R) in splits for c in letters]
    # 删除操作
    deletes = [L + R[1:] for (L, R) in splits if R]
    # 替换操作
    replaces = [L + c + R[1:] for (L, R) in splits if R for c in letters]

    return set(inserts + deletes + replaces)

def generate_edit_two(str):
    """
    给定一个字符串，生成编辑距离为 2 的字符串列表
    """
    # 很简单，也就是两层 "生成编辑距离为1"，的结果结果叠加
    return [e2 for e1 in generate_edit_one(str) for e2 in generate_edit_one(e1)]

print("生成编辑距离为 1 的单词，一共有: ", len(generate_edit_one("apple")))
print("生成编辑距离为 2 的单词，一共有: ", len(generate_edit_two("apple")))