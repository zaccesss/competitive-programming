class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        # Step 1: If lengths are different, they can never match
        # Rotation does NOT change string length
        if len(s) != len(goal):
            return False

        # Step 2: Combine string with itself
        # This creates all possible rotations inside one string
        # Example: "abcde" -> "abcdeabcde"
        doubled = s + s

        # Step 3: Check if goal exists inside the doubled string
        # If it does → goal is one of the rotations of s
        # If not → impossible to form by rotating
        return goal in doubled