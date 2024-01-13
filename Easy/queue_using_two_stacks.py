from collections import deque
class MyQueue:

    def __init__(self):
        self.q = deque()
        self.helper = deque()

    def __fix_q(self):
        if not self.q:
            while(self.helper):
                self.q.append(self.helper.pop())

    def push(self, x: int) -> None:
        self.helper.append(x)

    def pop(self) -> int:
        self.__fix_q()
        return self.q.pop()

    def peek(self) -> int:
        self.__fix_q()
        return self.q[-1]

    def empty(self) -> bool:
        return not self.q and not self.helper


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
