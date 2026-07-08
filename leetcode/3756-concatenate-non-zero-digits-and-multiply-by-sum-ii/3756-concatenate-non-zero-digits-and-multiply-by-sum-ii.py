class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10 ** 9 + 7

        # stored the positions and values of the non-zero digits
        positions = []
        digits = []

        for i, ch in enumerate(s):
            if ch != "0":
                positions.append(i)
                digits.append(int(ch))

        m = len(digits)

        # built the powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # built the prefix values of the concatenated number
        prefixNum = [0] * (m + 1)
        for i in range(m):
            prefixNum[i + 1] = (prefixNum[i] * 10 + digits[i]) % MOD

        # built the prefix sums of the digits
        prefixSum = [0] * (m + 1)
        for i in range(m):
            prefixSum[i + 1] = prefixSum[i] + digits[i]

        from bisect import bisect_left, bisect_right

        answer = []

        for left, right in queries:

            # found the non-zero digits inside the query range
            l = bisect_left(positions, left)
            r = bisect_right(positions, right) - 1

            # returned 0 if there were no non-zero digits
            if l > r:
                answer.append(0)
                continue

            length = r - l + 1

            # extracted the concatenated number modulo MOD
            x = (
                prefixNum[r + 1]
                - prefixNum[l] * pow10[length]
            ) % MOD

            # calculated the sum of the digits
            digitSum = prefixSum[r + 1] - prefixSum[l]

            # stored the answer
            answer.append((x * digitSum) % MOD)

        return answer