from collections import deque

class MyStack:

    def __init__(self):

        # Used one queue to simulate a stack
        self.q = deque()

    def push(self, x: int) -> None:

        # Added the new element to the queue
        self.q.append(x)

        # Moved previous elements behind the new element
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:

        # Removed and returned the top element
        return self.q.popleft()

    def top(self) -> int:

        # Returned the top element
        return self.q[0]

    def empty(self) -> bool:

        # Returned True if the queue is empty
        return len(self.q) == 0