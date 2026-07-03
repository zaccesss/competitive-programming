class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        # Number of rows
        rows = len(boxGrid)

        # Number of columns
        cols = len(boxGrid[0])

        # Process each row one by one
        for r in range(rows):

            # This points to where the next stone should fall
            # Start from the far right side
            empty = cols - 1

            # Move from right to left
            for c in range(cols - 1, -1, -1):

                # If we hit an obstacle
                if boxGrid[r][c] == '*':

                    # Stones cannot pass obstacles
                    # Reset empty position to left side of obstacle
                    empty = c - 1

                # If we find a stone
                elif boxGrid[r][c] == '#':

                    # Remove stone from current position
                    boxGrid[r][c] = '.'

                    # Move stone to the empty position
                    boxGrid[r][empty] = '#'

                    # Move empty pointer left
                    empty -= 1

        # Create rotated matrix
        # New size becomes cols x rows
        rotated = []

        # Build rotated matrix row by row
        for c in range(cols):

            new_row = []

            # Read original rows backwards
            for r in range(rows - 1, -1, -1):

                new_row.append(boxGrid[r][c])

            rotated.append(new_row)

        return rotated