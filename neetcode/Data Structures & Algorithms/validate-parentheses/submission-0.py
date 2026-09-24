class Solution:
    def isValid(self, s: str) -> bool:

        # used a stack to store opening brackets
        stack = []

        # used a dictionary to match closing brackets
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # looped through every character in the string
        for char in s:

            # added opening brackets to the stack
            if char in "({[":
                stack.append(char)

            else:
                # returned False if the stack is empty
                # or the brackets do not match
                if not stack or stack[-1] != pairs[char]:
                    return False

                # removed the matching opening bracket
                stack.pop()

        # returned True if all brackets were matched
        return len(stack) == 0