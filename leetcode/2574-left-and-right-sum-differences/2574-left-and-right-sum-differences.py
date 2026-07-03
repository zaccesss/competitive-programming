class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        total = sum(nums)
        left = 0
        answer = []

        for num in nums:
            # Computed right sum
            right = total - left - num

            # Added difference
            answer.append(abs(left - right))

            # Updated left sum
            left += num

        # Returned answer
        return answer