class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        # used freq to count candy costs.
        freq = [0] * 101

        # counted occurrences of each cost.
        for c in cost:
            freq[c] += 1

        # used total to store answer.
        total = 0

        # used position to track every third candy.
        position = 0

        # processed costs from largest to smallest.
        for value in range(100, 0, -1):

            while freq[value] > 0:

                # added candy cost unless it was free.
                if position % 3 != 2:
                    total += value

                position += 1
                freq[value] -= 1

        # returned minimum cost.
        return total