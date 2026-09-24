class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # if the array has 0 or 1 element, it's already sorted, so return it
        if len(nums) <= 1:
            return nums
        
        # find the middle point of the array
        mid = len(nums) // 2
        
        # recursively sort the left half (everything before middle)
        left = self.sortArray(nums[:mid])
        
        # recursively sort the right half (everything after middle)
        right = self.sortArray(nums[mid:])
        
        # merge the two sorted halves together and return
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        # this function takes two sorted arrays and merges them into one sorted array
        
        result = []
        
        # i and j are pointers that track where we are in each array
        i = 0  # pointer for left array
        j = 0  # pointer for right array
        
        # loop while we still have elements in both arrays to compare
        while i < len(left) and j < len(right):
            # compare the current elements from left and right
            if left[i] <= right[j]:
                # if left element is smaller, add it to result and move left pointer forward
                result.append(left[i])
                i += 1
            else:
                # if right element is smaller, add it to result and move right pointer forward
                result.append(right[j])
                j += 1
        
        # after one array is empty, add all remaining elements from left array
        result.extend(left[i:])
        
        # add all remaining elements from right array
        result.extend(right[j:])
        
        # return the merged sorted array
        return result