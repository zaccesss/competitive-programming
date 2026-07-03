class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0              # boundary: everything before this is 0
        mid = 0              # current element being examined
        high = len(nums) - 1 # boundary: everything after this is 2

        while mid <= high:   # keep going until mid and high meet
            if nums[mid] == 0:
                # swap current element with the low boundary
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1     # expand the 0-zone to the right
                mid += 1     # move to the next unseen element
            elif nums[mid] == 1:
                mid += 1     # 1 is already in the right place, just skip
            else:
                # swap current element with the high boundary
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1    # expand the 2-zone to the left
                             # don't move mid, the swapped value is unseen