class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def _import_to_outstack(self):
        if not self.out_stack:
            while self.in_stack:
                x = self.in_stack.pop()
                self.out_stack.append(x)

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._import_to_outstack()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._import_to_outstack()
        return self.out_stack[-1]

    def empty(self) -> bool:
        self._import_to_outstack()
        return False if self.out_stack else True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()