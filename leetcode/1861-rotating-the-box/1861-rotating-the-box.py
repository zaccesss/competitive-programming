class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        # number of rows
        rows = len(boxGrid)

        # number of columns
        cols = len(boxGrid[0])

        # process each row one by one
        for r in range(rows):

            # this points to where the next stone should fall
            # start from the far right side
            empty = cols - 1

            # move from right to left
            for c in range(cols - 1, -1, -1):

                # if we hit an obstacle
                if boxGrid[r][c] == '*':

                    # stones cannot pass obstacles
                    # reset empty position to left side of obstacle
                    empty = c - 1

                # if we find a stone
                elif boxGrid[r][c] == '#':

                    # remove stone from current position
                    boxGrid[r][c] = '.'

                    # move stone to the empty position
                    boxGrid[r][empty] = '#'

                    # move empty pointer left
                    empty -= 1

        # create rotated matrix
        # new size becomes cols x rows
        rotated = []

        # build rotated matrix row by row
        for c in range(cols):

            new_row = []

            # read original rows backwards
            for r in range(rows - 1, -1, -1):

                new_row.append(boxGrid[r][c])

            rotated.append(new_row)

        return rotated