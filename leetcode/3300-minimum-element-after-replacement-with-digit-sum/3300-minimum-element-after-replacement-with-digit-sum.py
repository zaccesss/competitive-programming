class Solution:
    def minElement(self, nums: List[int]) -> int:

        # Used result to store minimum digit sum.
        result = float("inf")

        # Looped through every number in nums.
        for num in nums:

            # Used total to store current digit sum.
            total = 0

            # Looped through every digit in number.
            while num > 0:

                # Added last digit to total.
                total += num % 10

                # Removed last digit from number.
                num //= 10

            # Updated minimum digit sum.
            result = min(result, total)

        # Returned smallest digit sum.
        return result