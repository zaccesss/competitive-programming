class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        # use sets to track numbers we have seen
        rows = {}
        cols = {}
        boxes = {}

        # go through every cell in the board
        for r in range(9):
            for c in range(9):

                # current value
                num = board[r][c]

                # skip empty cells
                if num == ".":
                    continue

                # identify which 3x3 box this cell belongs to
                # example:
                # (0,0) -> box (0,0)
                # (1,2) -> box (0,0)
                # (4,7) -> box (1,2)
                box_key = (r // 3, c // 3)

                # create sets if they do not exist yet
                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set()

                if box_key not in boxes:
                    boxes[box_key] = set()

                # check if number already exists
                # in row, column or box
                if (
                    num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_key]
                ):
                    return False

                # add number into tracking sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_key].add(num)

        # if no duplicates were found
        return True