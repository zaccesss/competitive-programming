class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # pointer tracking position of next valid element
        for num in nums:  # loop through every number
            if num != val:  # if the number is not the one to remove
                nums[k] = num  # place it at position k
                k += 1  # move the pointer forward
        return k  # return count of remaining elements