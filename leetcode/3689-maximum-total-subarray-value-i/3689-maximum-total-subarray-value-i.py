class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        # Used maximum and minimum values in the array.
        max_val = max(nums)
        min_val = min(nums)

        # Returned the maximum total value.
        return k * (max_val - min_val)