class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        candidate1 = candidate2 = None  # store possible majority elements
        count1 = count2 = 0  # counts for each candidate

        for num in nums:

            if num == candidate1:  # same as candidate1
                count1 += 1

            elif num == candidate2:  # same as candidate2
                count2 += 1

            elif count1 == 0:  # replace candidate1 if count1 is empty
                candidate1 = num
                count1 = 1

            elif count2 == 0:  # replace candidate2 if count2 is empty
                candidate2 = num
                count2 = 1

            else:  # different from both candidates
                count1 -= 1
                count2 -= 1

        result = []

        if nums.count(candidate1) > len(nums) // 3:  # verify candidate1
            result.append(candidate1)

        if candidate2 != candidate1 and nums.count(candidate2) > len(nums) // 3:  # verify candidate2
            result.append(candidate2)

        return result