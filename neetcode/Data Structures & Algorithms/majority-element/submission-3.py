class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}  # stores frequency of each number
        n = len(nums)
        for num in nums:
            count[num] = count.get(num, 0) + 1  # increment count
            if count[num] > n // 2:  # if it exceeds n/2, it's the majority
                return num