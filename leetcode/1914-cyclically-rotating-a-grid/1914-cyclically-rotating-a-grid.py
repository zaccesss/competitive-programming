class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        rows = len(grid)
        cols = len(grid[0])

        layers = min(rows, cols) // 2  # total layers

        for layer in range(layers):

            elements = []

            top = layer
            bottom = rows - layer - 1
            left = layer
            right = cols - layer - 1

            for c in range(left, right + 1):  # top row
                elements.append(grid[top][c])

            for r in range(top + 1, bottom):  # right column
                elements.append(grid[r][right])

            for c in range(right, left - 1, -1):  # bottom row
                elements.append(grid[bottom][c])

            for r in range(bottom - 1, top, -1):  # left column
                elements.append(grid[r][left])

            rotate = k % len(elements)  # reduce extra rotations

            rotated = (
                elements[rotate:] + elements[:rotate]
            )  # rotate left

            idx = 0

            for c in range(left, right + 1):  # refill top row
                grid[top][c] = rotated[idx]
                idx += 1

            for r in range(top + 1, bottom):  # refill right column
                grid[r][right] = rotated[idx]
                idx += 1

            for c in range(right, left - 1, -1):  # refill bottom row
                grid[bottom][c] = rotated[idx]
                idx += 1

            for r in range(bottom - 1, top, -1):  # refill left column
                grid[r][left] = rotated[idx]
                idx += 1

        return grid