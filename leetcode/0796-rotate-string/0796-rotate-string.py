class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # step 1: If lengths are different, they can never match
        # rotation does NOT change string length
        if len(s) != len(goal):
            return False

        # step 2: Combine string with itself
        # this creates all possible rotations inside one string
        # example: "abcde" -> "abcdeabcde"
        doubled = s + s

        # step 3: Check if goal exists inside the doubled string
        # if it does → goal is one of the rotations of s
        # if not → impossible to form by rotating
        return goal in doubled