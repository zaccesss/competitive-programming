class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        from bisect import bisect_left, bisect_right

        MOD = 1000000007

        positions = []
        digits = []

        # collected the non-zero digits and their positions
        for i, ch in enumerate(s):
            if ch != "0":
                positions.append(i)
                digits.append(ord(ch) - 48)

        m = len(digits)

        # built the powers of 10
        pow10 = [1] * (m + 1)
        for i in range(m):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        # built the prefix values of the concatenated number
        prefixNum = [0] * (m + 1)
        value = 0
        for i, d in enumerate(digits):
            value = (value * 10 + d) % MOD
            prefixNum[i + 1] = value

        # built the prefix sums of the digits
        prefixSum = [0] * (m + 1)
        total = 0
        for i, d in enumerate(digits):
            total += d
            prefixSum[i + 1] = total

        pos = positions
        preNum = prefixNum
        preSum = prefixSum
        p10 = pow10
        ans = []

        # answered each query
        for l, r in queries:

            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            length = right - left

            x = (preNum[right] - preNum[left] * p10[length]) % MOD
            digitSum = preSum[right] - preSum[left]

            ans.append((x * digitSum) % MOD)

        return ans