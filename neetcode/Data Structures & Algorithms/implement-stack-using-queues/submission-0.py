from collections import deque

class MyStack:

    def __init__(self):

        # used one queue to simulate a stack
        self.q = deque()

    def push(self, x: int) -> None:

        # added the new element to the queue
        self.q.append(x)

        # moved previous elements behind the new element
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:

        # removed and returned the top element
        return self.q.popleft()

    def top(self) -> int:

        # returned the top element
        return self.q[0]

    def empty(self) -> bool:

        # returned True if the queue is empty
        return len(self.q) == 0