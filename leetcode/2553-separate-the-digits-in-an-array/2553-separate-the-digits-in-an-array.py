class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        # Store final separated digits
        answer = []

        # Go through each number in nums
        for num in nums:

            # Convert number to string
            # Then loop through each digit character
            for digit in str(num):

                # Convert digit back to integer
                answer.append(int(digit))

        return answer