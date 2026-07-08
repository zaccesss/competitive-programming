class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:

        MOD = 10 ** 9 + 7
        n = len(s)

        # stored the positions and values of the non-zero digits
        positions = []
        digits = []

        # mapped each string position to its index in the non-zero list
        nextNonZero = [-1] * n
        prevNonZero = [-1] * n

        for i, ch in enumerate(s):
            if ch != "0":
                positions.append(i)
                digits.append(int(ch))

        m = len(digits)

        # built the mapping to the previous non-zero digit
        idx = -1
        for i in range(n):
            if idx + 1 < m and positions[idx + 1] == i:
                idx += 1
            prevNonZero[i] = idx

        # built the mapping to the next non-zero digit
        idx = m
        for i in range(n - 1, -1, -1):
            if idx - 1 >= 0 and positions[idx - 1] == i:
                idx -= 1
            if idx == m:
                nextNonZero[i] = -1
            else:
                nextNonZero[i] = idx

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

        answer = []

        for left, right in queries:

            # found the first and last non-zero digits in the range
            l = nextNonZero[left]
            r = prevNonZero[right]

            # returned 0 if there were no non-zero digits
            if l == -1 or r == -1 or l > r:
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