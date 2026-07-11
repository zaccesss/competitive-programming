class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        # searched the matrix using binary search
        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            # converted the index back into row and column
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            # found the target
            if value == target:
                return True

            # searched the right half
            if value < target:
                left = mid + 1

            # searched the left half
            else:
                right = mid - 1

        # the target does not exist
        return False