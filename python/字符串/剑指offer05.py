"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。v

"""


class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")
