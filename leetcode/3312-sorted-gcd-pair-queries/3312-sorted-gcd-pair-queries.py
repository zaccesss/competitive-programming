from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Count frequency of each number
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # Count numbers divisible by each gcd
        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            for x in range(g, mx + 1, g):
                cnt[g] += freq[x]

        # Count pairs with gcd exactly g
        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            exact[g] = cnt[g] * (cnt[g] - 1) // 2
            for x in range(g * 2, mx + 1, g):
                exact[g] -= exact[x]

        # Prefix count of sorted gcd values
        pref = []
        s = 0
        for g in range(1, mx + 1):
            s += exact[g]
            pref.append(s)

        # Answer each query
        return [bisect_right(pref, q) + 1 for q in queries]