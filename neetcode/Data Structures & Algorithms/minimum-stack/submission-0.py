class MinStack:

    def __init__(self):

        # used stack to store all values.
        self.stack = []

        # used minStack to store minimum values.
        self.minStack = []

    def push(self, val: int) -> None:

        # added value to main stack.
        self.stack.append(val)

        # added first value as current minimum.
        if not self.minStack:
            self.minStack.append(val)

        # added minimum between current value and previous minimum.
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:

        # removed top value from main stack.
        self.stack.pop()

        # removed corresponding minimum value.
        self.minStack.pop()

    def top(self) -> int:

        # returned top value from main stack.
        return self.stack[-1]

    def getMin(self) -> int:

        # returned current minimum value.
        return self.minStack[-1]