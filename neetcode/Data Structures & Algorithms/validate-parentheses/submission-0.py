class Solution:
    def isValid(self, s: str) -> bool:

        # Used a stack to store opening brackets
        stack = []

        # Used a dictionary to match closing brackets
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # Looped through every character in the string
        for char in s:

            # Added opening brackets to the stack
            if char in "({[":
                stack.append(char)

            else:
                # Returned False if the stack is empty
                # or the brackets do not match
                if not stack or stack[-1] != pairs[char]:
                    return False

                # Removed the matching opening bracket
                stack.pop()

        # Returned True if all brackets were matched
        return len(stack) == 0