class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        total = sum(nums)
        left = 0
        answer = []

        for num in nums:
            # computed right sum
            right = total - left - num

            # added difference
            answer.append(abs(left - right))

            # updated left sum
            left += num

        # returned answer
        return answer