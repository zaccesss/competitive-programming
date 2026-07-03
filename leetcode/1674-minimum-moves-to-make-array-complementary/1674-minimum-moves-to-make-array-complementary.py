class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:

        diff = [0] * (2 * limit + 2)
        n = len(nums)
        half = n // 2

        for i in range(half):

            a = nums[i]
            b = nums[n - 1 - i]

            if a > b:
                a, b = b, a

            s = a + b

            diff[2] += 2
            diff[a + 1] -= 1
            diff[s] -= 1
            diff[s + 1] += 1
            diff[b + limit + 1] += 1

        best = n
        cur = 0

        for x in range(2, 2 * limit + 1):
            cur += diff[x]

            if cur < best:
                best = cur

        return best