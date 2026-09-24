class MyQueue:

    def __init__(self):

        # used two stacks to simulate a queue
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:

        # added new elements into the input stack
        self.in_stack.append(x)

    def pop(self) -> int:

        # moved elements only if out_stack is empty
        if not self.out_stack:

            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # removed and returned the front element
        return self.out_stack.pop()

    def peek(self) -> int:

        # moved elements only if out_stack is empty
        if not self.out_stack:

            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

        # returned the front element
        return self.out_stack[-1]

    def empty(self) -> bool:

        # returned True if both stacks are empty
        return not self.in_stack and not self.out_stack