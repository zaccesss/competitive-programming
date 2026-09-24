class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        # used maximum and minimum values in the array.
        max_val = max(nums)
        min_val = min(nums)

        # returned the maximum total value.
        return k * (max_val - min_val)