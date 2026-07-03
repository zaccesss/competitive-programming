class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate1 = candidate2 = None  # possible majority elements
        count1 = count2 = 0  # counts for each candidate

        # Boyer-Moore Voting Algorithm
        for num in nums:

            if num == candidate1:  # increase count for candidate1
                count1 += 1

            elif num == candidate2:  # increase count for candidate2
                count2 += 1

            elif count1 == 0:  # replace candidate1
                candidate1 = num
                count1 = 1

            elif count2 == 0:  # replace candidate2
                candidate2 = num
                count2 = 1

            else:  # cancel out different numbers
                count1 -= 1
                count2 -= 1

        # manually count occurrences instead of using nums.count()
        # avoids scanning the array multiple times

        count1 = 0
        count2 = 0

        for num in nums:

            if num == candidate1:
                count1 += 1

            elif num == candidate2:
                count2 += 1

        result = []

        if count1 > len(nums) // 3:  # verify candidate1
            result.append(candidate1)

        if count2 > len(nums) // 3:  # verify candidate2
            result.append(candidate2)

        return result