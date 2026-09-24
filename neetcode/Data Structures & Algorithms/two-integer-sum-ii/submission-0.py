class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # used left pointer at the beginning of array.
        left = 0

        # used right pointer at the end of array.
        right = len(numbers) - 1

        # looped until valid pair was found.
        while left < right:

            # calculated current sum.
            currentSum = numbers[left] + numbers[right]

            # returned indices if target was found.
            if currentSum == target:
                return [left + 1, right + 1]

            # moved right pointer if sum was too large.
            elif currentSum > target:
                right -= 1

            # moved left pointer if sum was too small.
            else:
                left += 1