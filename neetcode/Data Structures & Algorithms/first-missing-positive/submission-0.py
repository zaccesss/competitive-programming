class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Place each number in its correct index
        # 1 should be at index 0
        # 2 should be at index 1
        # etc.
        for i in range(n):
            while (
                1 <= nums[i] <= n
                and nums[nums[i] - 1] != nums[i]
            ):
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]

        # Find the first index where value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct
        return n + 1