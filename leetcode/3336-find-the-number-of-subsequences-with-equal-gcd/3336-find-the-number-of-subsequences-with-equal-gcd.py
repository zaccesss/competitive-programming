from math import gcd
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:

        MOD = 10 ** 9 + 7

        # dp[(g1, g2)] = number of ways
        # g1 = gcd of first subsequence
        # g2 = gcd of second subsequence
        dp = {(0, 0): 1}

        for num in nums:

            newDP = defaultdict(int)

            for (g1, g2), count in dp.items():

                # skip current element
                newDP[(g1, g2)] = (newDP[(g1, g2)] + count) % MOD

                # add to first subsequence
                newG1 = num if g1 == 0 else gcd(g1, num)
                newDP[(newG1, g2)] = (newDP[(newG1, g2)] + count) % MOD

                # add to second subsequence
                newG2 = num if g2 == 0 else gcd(g2, num)
                newDP[(g1, newG2)] = (newDP[(g1, newG2)] + count) % MOD

            dp = newDP

        answer = 0

        for (g1, g2), count in dp.items():
            if g1 != 0 and g1 == g2:
                answer = (answer + count) % MOD

        return answer