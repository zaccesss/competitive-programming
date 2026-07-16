from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        pre = []
        mx = 0

        # Build prefix GCD array
        for x in nums:
            mx = max(mx, x)
            pre.append(gcd(x, mx))

        # Sort the prefix GCDs
        pre.sort()

        ans = 0
        l, r = 0, len(pre) - 1

        # Pair smallest with largest
        while l < r:
            ans += gcd(pre[l], pre[r])
            l += 1
            r -= 1

        return ans