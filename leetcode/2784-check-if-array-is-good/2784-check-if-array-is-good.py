class Solution:
    def isGood(self, nums: List[int]) -> bool:

        # Sort the array
        nums.sort()

        # Largest number in the array
        n = nums[-1]

        # A valid base[n] must have length n + 1
        # Example:
        # base[3] = [1,2,3,3] -> length 4
        if len(nums) != n + 1:
            return False

        # Check that numbers from 1 to n-1
        # appear exactly once
        for i in range(n - 1):

            # Expected number at index i is i + 1
            if nums[i] != i + 1:
                return False

        # Last two elements must both equal n
        return nums[-1] == n and nums[-2] == n