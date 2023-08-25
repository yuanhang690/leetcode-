"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

技巧：在匹配左括号的时候，
右括号先入栈，就只需要比较当前元素和栈顶相不相等就可以了，比左括号先入栈代码实现要简单的多了！

"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 长度为奇数一定不符合要求
        if len(s) % 2 != 0:
            return False
        stack = []

        for item in s:
            if item == "(":
                stack.append(")")
            elif item == "[":
                stack.append("]")
            elif item == "{":
                stack.append("}")
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        # 栈为空说明匹配成功
        return True if not stack else False
