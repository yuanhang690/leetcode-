"""
383. 赎金信
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

# 简介Counter作用:

from collections import Counter

lst = [1, 2, 3, 1, 2, 1, 4, 5, 3]
counter = Counter(lst)
counter 现在包含的内容将类似于 Counter({1: 3, 2: 2, 3: 2, 4: 1, 5: 1})

"""
import collections
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         # 剪枝
#         # 当magazine的长度小于ransomNote的长度时一定不满足
#         if len(magazine)<len(ransomNote):
#             return False
#         # 方法一：哈希表
#         # hash = {}
#         # #　把magazine的字母存入字典并计数
#         # for i in magazine:
#         #     if i in hash:
#         #         hash[i] +=1
#         #     else:
#         #         hash[i] = 1

#         # # 遍历第一个字符串，不在字典或次数为0时说明不满足条件
#         # for v in ransomNote:
#         #     if v not in hash or hash[v]==0:
#         #         return False
#         #     else:
#         #         hash[v] -=1
#         # return True
#         # 方法二计数
#         return not collections.Counter(ransomNote)-collections.Counter(magazine)


s = "abcdefafaf"
s2 = "wdadadadwad"

print(collections.Counter(s))
print(collections.Counter(s2))
print(collections.Counter(s)-collections.Counter(s2))
