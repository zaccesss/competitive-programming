class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # assign a rank to each unique value in sorted order
        rank = {}
        currentRank = 1

        for num in sorted(set(arr)):
            rank[num] = currentRank
            currentRank += 1

        # replace each value with its rank
        return [rank[num] for num in arr]