class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)                          # sum of all elements
        f = sum(i * nums[i] for i in range(n))    # F(0)
        
        result = f
        
        for k in range(1, n):
            # each rotation: add total, subtract n * element that wraps around
            f = f + total - n * nums[n - k]
            result = max(result, f)
        
        return result