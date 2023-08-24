from collections import deque


class MyStack:
    def __init__(self):
        """
        in:存放数据
        out:辅助pop
        """
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x: int) -> None:
        # 直接append
        self.queue_in.append(x)

    def pop(self) -> int:
        # 先判断是不是空的
        if self.empty():
            return None
        # 先把queue_in中的所有元素（除了最后一个），依次出列放进queue_out
        for i in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft())
        # 交换in和out
        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self) -> bool:
        return len(self.queue_in) == 0
