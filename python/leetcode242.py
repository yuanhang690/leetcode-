"""
有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1: 输入: s = "anagram", t = "nagaram" 输出: true

示例 2: 输入: s = "rat", t = "car" 输出: false
"""
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # 长度不相等时，返回false
        # if len(s) != len(t):
        #     return False
        
        # 使用字典按照 字母：次数   格式存储
        # 遍历s时，遇到相同字母，次数加一，遍历t，时次数减一，如果相同的话每个字母的value应该都是0

        # hash = {}
        # for c in s:
        #     try:
        #         hash[c] +=1
        #     except:
        #         hash[c] = 1

        # for r in t:
        #     try:
        #         hash[r] -=1
        #     except:
        #         hash[r] = 1

        # for val in hash.values():
        #     if val !=0:
        #         return False
            
        # return True
        # 优化：
        if len(s) != len(t):
            return False
        """
        创建了一个默认值为整数 0 的 defaultdict 对象。
        这意味着，如果你访问字典 dic 中不存在的键，该键会被自动插入到字典中，并且对应的值会被初始化为 0
        
        """
        hash = defaultdict(int)
        for c in s:
            hash[c] +=1

        for d in t:
            hash[d] -=1

        for val in hash.values():
            if val !=0:
                return False
        return True

        


