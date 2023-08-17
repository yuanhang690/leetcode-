"""
28. 找出字符串中第一个匹配项的下标
(kmp算法)

"""


class Solution:
    def getNext(self, next: list, s: str) -> list:
        """
        用i指向后缀末尾
        j指向前缀末尾
        """
        j = -1
        next[0] = j
        for i in range(1, len(s)):
            # 不同时：
            while j >= 0 and s[i] != s[j + 1]:
                # 将j回退
                j = next[j]
            if s[i] == s[j + 1]:
                # 相同时j往前移动
                j += 1
            next[i] = j

        return next

    def strStr(self, haystack: str, needle: str) -> int:
        # 计算next数组
        next = [0] * len(needle)
        next = self.getNext(next, needle)
        j = -1
        for i in range(len(haystack)):
            while j >= 0 and haystack[i] != needle[j + 1]:
                # 回退
                j = next[j]

            if haystack[i] == needle[j + 1]:
                j += 1

            if j == len(needle) - 1:
                return i - len(needle) + 1
        return -1
