class Solution:
    def minimumCost(self, cost: List[int]) -> int:

        # Used freq to count candy costs.
        freq = [0] * 101

        # Counted occurrences of each cost.
        for c in cost:
            freq[c] += 1

        # Used total to store answer.
        total = 0

        # Used position to track every third candy.
        position = 0

        # Processed costs from largest to smallest.
        for value in range(100, 0, -1):

            while freq[value] > 0:

                # Added candy cost unless it was free.
                if position % 3 != 2:
                    total += value

                position += 1
                freq[value] -= 1

        # Returned minimum cost.
        return total