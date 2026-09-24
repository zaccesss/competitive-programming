class Solution:
    def firstMissingPositive(
        self,
        nums: List[int]
    ) -> int:

        n = len(nums)

        # placed each valid number into its correct index.
        for i in range(n):

            while (
                nums[i] > 0
                and nums[i] <= n
                and nums[i]
                != nums[nums[i] - 1]
            ):

                j = nums[i] - 1

                nums[i], nums[j] = (
                    nums[j],
                    nums[i]
                )

        # found first missing positive.
        for i in range(n):

            if nums[i] != i + 1:

                return i + 1

        # all numbers 1..n exist.
        return n + 1