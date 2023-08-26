"""
 删除字符串中的所有相邻重复项

 
 给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        # stack = []
        # stack.append(s[0])
        # for i in range(1, len(s)):
        #     if len(stack) == 0:
        #         stack.append(s[i])
        #     elif stack[-1] == s[i]:
        #         stack.pop()
        #     else:
        #         stack.append(s[i])
        # 优化
        stack = []
        for val in s:
            if stack and stack[-1] == val:
                stack.pop()
            else:
                stack.append(val)

        return "".join(stack)


Solution1 = Solution()

s = "abbaca"
print(Solution1.removeDuplicates(s))
