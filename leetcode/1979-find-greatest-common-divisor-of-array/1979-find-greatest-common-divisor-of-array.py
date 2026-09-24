class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # find the smallest and largest numbers
        mn = min(nums)
        mx = max(nums)

        # compute their GCD
        while mx:
            mn, mx = mx, mn % mx

        return mn