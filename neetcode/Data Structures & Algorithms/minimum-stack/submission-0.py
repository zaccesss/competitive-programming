class MinStack:

    def __init__(self):

        # Used stack to store all values.
        self.stack = []

        # Used minStack to store minimum values.
        self.minStack = []

    def push(self, val: int) -> None:

        # Added value to main stack.
        self.stack.append(val)

        # Added first value as current minimum.
        if not self.minStack:
            self.minStack.append(val)

        # Added minimum between current value and previous minimum.
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:

        # Removed top value from main stack.
        self.stack.pop()

        # Removed corresponding minimum value.
        self.minStack.pop()

    def top(self) -> int:

        # Returned top value from main stack.
        return self.stack[-1]

    def getMin(self) -> int:

        # Returned current minimum value.
        return self.minStack[-1]