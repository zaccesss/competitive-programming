class Solution:
    def minElement(self, nums: List[int]) -> int:

        # used result to store minimum digit sum.
        result = float("inf")

        # looped through every number in nums.
        for num in nums:

            # used total to store current digit sum.
            total = 0

            # looped through every digit in number.
            while num > 0:

                # added last digit to total.
                total += num % 10

                # removed last digit from number.
                num //= 10

            # updated minimum digit sum.
            result = min(result, total)

        # returned smallest digit sum.
        return result