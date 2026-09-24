class Solution:
    def isGood(self, nums: List[int]) -> bool:

        # sort the array
        nums.sort()

        # largest number in the array
        n = nums[-1]

        # a valid base[n] must have length n + 1
        # example:
        # base[3] = [1,2,3,3] -> length 4
        if len(nums) != n + 1:
            return False

        # check that numbers from 1 to n-1
        # appear exactly once
        for i in range(n - 1):

            # expected number at index i is i + 1
            if nums[i] != i + 1:
                return False

        # last two elements must both equal n
        return nums[-1] == n and nums[-2] == n