class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Find the smallest and largest numbers
        mn = min(nums)
        mx = max(nums)

        # Compute their GCD
        while mx:
            mn, mx = mx, mn % mx

        return mn