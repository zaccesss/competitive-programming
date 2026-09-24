class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:

        n = len(nums)

        # store minimum value from the right side
        suffix_min = [0] * n

        suffix_min[-1] = nums[-1]

        # build suffix minimum array
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        ans = [0] * n

        start = 0
        current_max = nums[0]

        # find connected components
        for i in range(n - 1):

            # update current maximum in this component
            current_max = max(current_max, nums[i])

            # if there is an inversion ahead,
            # component must continue
            if current_max > suffix_min[i + 1]:
                continue

            # otherwise component ends here
            for j in range(start, i + 1):
                ans[j] = current_max

            # start new component
            start = i + 1

            if start < n:
                current_max = nums[start]

        # fill last component
        current_max = max(nums[start:])

        for i in range(start, n):
            ans[i] = current_max

        return ans