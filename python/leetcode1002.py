"""
查找共用字符
给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），
并以数组形式返回。你可以按 任意顺序 返回答案。

"""
from collections import defaultdict,Counter
class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # #　统计每个字符出现的最小频率
        # if not words:
        #     return []
        # result = []
        # # 用第一个字符串将hash初始化
        # hash = [0]*26
        # for i,c in enumerate(words[0]):
        #     # 统计除第一个字符串外字符的出现频率
        #     hash[ord(c)-ord('a')] +=1


        # # 统计第一个字符意外的出现频率
        # for i in range(1,len(words)):
        #     hash_order = [0]*26

        #     for j in range(len(words[i])):
        #         hash_order[ord(words[i][j])-ord('a')] +=1

        #     # 更新hash
        #     for k in range(26):
        #         hash[k] = min(hash[k],hash_order[k])
        # # 把hash的统计转换成输出形式
        # for i in range(26):
        #     # hash[i]==0时，说明不是每个字符串都有这个字符
        #     while hash[i]!=0:
        #         #　换成对应ａｓｃｉｌ码，转换成字符，加入ｒｅｓｕｌｔ中
        #         result.extend(chr(i+ord('a')))
        #         hash[i] -=1
        # return result

        #　解法二：
        res = None
        for a in words:
            # 计数器
            count = Counter(a)
            # 将返回一个类似于 {'a': 2, 'b': 2, 'c': 1} 的字典
            if res ==None:
                res = count
            else:
                res &= res
        # 返回迭代器
        
        return list(res.elements())




