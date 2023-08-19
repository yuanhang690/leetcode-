"""

459. 重复的子字符串
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。


"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 长度小于等于1，一定不存在
        n = len(s)
        if n <= 1:
            return False
        """
        如果满足题意的话，那么s长度一定是子串长度的倍数，
        子串至少要重复一次，所以长度不会大于主串的一半
        """
        substr = ""
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substr = s[:i]
                if substr * (n // i) == s:
                    return True
        return False
