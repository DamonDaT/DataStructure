dic = ["创新", "工场", "创新工场", "人", "人工", "人工智能", "智能", "工程院", "工程", "深圳",
       "设立", "大湾区", "湾区", "研究", "研究院"]

text1 = "创新工场人工智能工程院在深圳设立大湾区研究院"

'''
# 正向最大匹配法
# 1 从左向右取待分汉语句的m个字作为匹配字段，m为词典中最长词的长度
# 2 查找词典进行匹配
# 3 若匹配成功，则将该字段作为一个词切分出去
# 4 若匹配不成功，则将该字段最后一个字去掉，剩下的字作为新匹配字段，进行再次匹配
# 5 重复上述过程，直到切分所有词为止
'''
class FMM(object):
    def __init__(self,word_dict):
        self.word_dict = word_dict
        self.window_size = self.__getMaxLen()

    # 获取字典中词的最大长度
    def __getMaxLen(self):
        return max(map(len,[w for w in self.word_dict]))

    # 分词
    def cut(self,text):
        result = []
        index = 0
        # 输入字符串的长度
        text_size = len(text)
        while text_size > index:
            for size in range(self.window_size + index, index, -1):
                piece = text[index:size]
                if piece in self.word_dict:
                    index = size - 1
                    break
            index = index + 1
            result.append(piece)
        return result

tokenizer = FMM(dic)
print('/'.join(tokenizer.cut(text1)))


'''
# 反向最大匹配法
# 1 RMM的基本原理与FMM基本相同，不同的是分词的方向与FMM相反。
# 2 RMM是从待分词句子的末端开始，也就是从右向左开始匹配扫描，每次取末端m个字作为匹配字段，
# 3 匹配失败，则去掉匹配字段前面的一个字，继续匹配
'''
class RMM(object):
    def __init__(self,word_dict):
        self.word_dict = word_dict
        self.window_size = self.__getMaxLen()

    # 获取字典中词的最大长度
    def __getMaxLen(self):
        return max(map(len,[w for w in self.word_dict]))

    # 分词
    def cut(self,text):
        result = []
        index = len(text)
        window_size = min(index,self.window_size)
        while index > 0:
            for size in range(index-window_size, index):
                piece = text[size:index]
                if piece in self.word_dict:
                    index = size + 1
                    break
            index = index - 1
            result.append(piece)
        result.reverse()
        return result


'''
# 双向最大匹配法
# 1 如果正反向分词结果词数不同，则取分词数量少的那个。
# 2 如果分词结果词数相同：
# 2.1 分词结果相同，没有歧义，返回任意一个。
# 2.2 分词结果不同，返回其中单字数量较少的那个。
'''
class BIMM(object):
    def __init__(self,word_dict):
        self.word_dict = word_dict
        self.FMM = FMM(self.word_dict)
        self.RMM = RMM(self.word_dict)

    def cut(self,text):
        res_fmm = self.FMM.cut(text)
        res_rmm = self.RMM.cut(text)
        if len(res_fmm) == len(res_rmm):
            if res_fmm == res_rmm :
                return res_fmm
            else:
                f_word_count = len([w for w in res_fmm if len(w)==1])
                r_word_count = len([w for w in res_rmm if len(w)==1])
                return res_fmm if f_word_count < r_word_count else res_rmm
        else:
            return res_fmm if len(res_fmm) < len(res_rmm) else res_rmm
