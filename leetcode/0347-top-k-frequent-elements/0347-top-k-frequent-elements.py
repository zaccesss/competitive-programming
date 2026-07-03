class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # sort by frequency descending and return top k keys
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]