class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):

        left = 0
        right = len(arr) - k

        # Binary search for the best starting index
        while left < right:

            mid = (left + right) // 2

            # Compare the leftmost and the new rightmost candidate
            if x - arr[mid] > arr[mid + k] - x:
                # Better window is to the right
                left = mid + 1
            else:
                # Better window is to the left (or equal)
                right = mid

        # Return the best window
        return arr[left:left + k]