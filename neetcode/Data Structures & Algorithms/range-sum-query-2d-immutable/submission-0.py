class NumMatrix:

    def __init__(self, matrix):
        # Get number of rows and columns
        rows, cols = len(matrix), len(matrix[0])

        # Create prefix sum matrix with extra row and column (all zeros)
        # This avoids index issues when calculating sums
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Build the prefix sum matrix
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):

                # Current value from original matrix
                current = matrix[r - 1][c - 1]

                # Build prefix sum using:
                # current cell
                # + sum above
                # + sum left
                # - overlap (to avoid double counting)
                self.prefix[r][c] = (
                    current
                    + self.prefix[r - 1][c]      # sum above
                    + self.prefix[r][c - 1]      # sum left
                    - self.prefix[r - 1][c - 1]  # remove overlap
                )

    def sumRegion(self, row1, col1, row2, col2):
        # We shift everything by +1 because prefix has padding

        # Total rectangle from (0,0) to (row2, col2)
        total = self.prefix[row2 + 1][col2 + 1]

        # Remove area above the rectangle
        top = self.prefix[row1][col2 + 1]

        # Remove area to the left of the rectangle
        left = self.prefix[row2 + 1][col1]

        # Add back the overlap (it was subtracted twice)
        overlap = self.prefix[row1][col1]

        # Final result
        return total - top - left + overlap