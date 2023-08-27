# https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/
from operator import add, sub, mul


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        option_map = {"+": add, "-": sub, "*": mul, "/": lambda x, y: int(x / y)}
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(option_map[token](op1, op2))
        return stack.pop()
