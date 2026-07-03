class Solution:
    def validPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1

        while left < right:

            # Found mismatch
            if s[left] != s[right]:

                # Check by skipping left character
                l1 = left + 1
                r1 = right
                ok1 = True

                while l1 < r1:
                    if s[l1] != s[r1]:
                        ok1 = False
                        break
                    l1 += 1
                    r1 -= 1

                # Check by skipping right character
                l2 = left
                r2 = right - 1
                ok2 = True

                while l2 < r2:
                    if s[l2] != s[r2]:
                        ok2 = False
                        break
                    l2 += 1
                    r2 -= 1

                return ok1 or ok2

            left += 1
            right -= 1

        return True