class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):

        left = 0
        right = len(arr) - k

        # binary search for the best starting index
        while left < right:

            mid = (left + right) // 2

            # compare the leftmost and the new rightmost candidate
            if x - arr[mid] > arr[mid + k] - x:
                # better window is to the right
                left = mid + 1
            else:
                # better window is to the left (or equal)
                right = mid

        # return the best window
        return arr[left:left + k]