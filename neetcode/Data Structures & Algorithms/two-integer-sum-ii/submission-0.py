class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Used left pointer at the beginning of array.
        left = 0

        # Used right pointer at the end of array.
        right = len(numbers) - 1

        # Looped until valid pair was found.
        while left < right:

            # Calculated current sum.
            currentSum = numbers[left] + numbers[right]

            # Returned indices if target was found.
            if currentSum == target:
                return [left + 1, right + 1]

            # Moved right pointer if sum was too large.
            elif currentSum > target:
                right -= 1

            # Moved left pointer if sum was too small.
            else:
                left += 1