"""
字符串反转2

给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)
        for cur in range(0, len(s), 2 * k):
            # res[cur: cur + k] 表示从列表 res 中从索引 cur 开始，取长度为 k 的子列表（或字符串的子串）
            res[cur : cur + k] = reverse_substring(res[cur : cur + k])

        return "".join(res)
