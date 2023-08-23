"""
232.用栈实现队列
借助两个栈，实现顺序：init、push、empty、pop、peek
"""


class MyQueue:
    def __init__(self):
        """
        in负责push，out负责pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """
        只要in获out不为空，说明队列不为空
        """
        return not (self.stack_in or self.stack_out)
