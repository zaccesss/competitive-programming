class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Used result to store valid quadruplets.
        result = []

        # Sorted the array.
        nums.sort()

        n = len(nums)

        # Fixed first number.
        for i in range(n - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Fixed second number.
            for j in range(i + 1, n - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = n - 1

                # Used two pointers for remaining numbers.
                while l < r:

                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total < target:
                        l += 1

                    elif total > target:
                        r -= 1

                    else:

                        result.append(
                            [nums[i], nums[j], nums[l], nums[r]]
                        )

                        l += 1
                        r -= 1

                        # Skipped duplicate left values.
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

                        # Skipped duplicate right values.
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

        # Returned all unique quadruplets.
        return result