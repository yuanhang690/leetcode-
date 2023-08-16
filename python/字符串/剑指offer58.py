"""

左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。b

"""


class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # s1 = s[:n]
        # s2 = s[n : len(s)]
        # # print(s1, s2)
        # return s2 + s1
        # 优化
        # 时间复杂度O(n)
        return s[n:] + s[:n]


solution = Solution()
s = "abcdefg"
res = solution.reverseLeftWords(s, 2)
print(res)
