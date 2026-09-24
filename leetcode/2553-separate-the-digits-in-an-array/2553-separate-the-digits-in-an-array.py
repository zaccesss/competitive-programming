class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        # store final separated digits
        answer = []

        # go through each number in nums
        for num in nums:

            # convert number to string
            # then loop through each digit character
            for digit in str(num):

                # convert digit back to integer
                answer.append(int(digit))

        return answer