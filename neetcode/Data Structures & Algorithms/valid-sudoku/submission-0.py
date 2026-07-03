class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        # Use sets to track numbers we have seen
        rows = {}
        cols = {}
        boxes = {}

        # Go through every cell in the board
        for r in range(9):
            for c in range(9):

                # Current value
                num = board[r][c]

                # Skip empty cells
                if num == ".":
                    continue

                # Identify which 3x3 box this cell belongs to
                # Example:
                # (0,0) -> box (0,0)
                # (1,2) -> box (0,0)
                # (4,7) -> box (1,2)
                box_key = (r // 3, c // 3)

                # Create sets if they do not exist yet
                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set()

                if box_key not in boxes:
                    boxes[box_key] = set()

                # Check if number already exists
                # in row, column or box
                if (
                    num in rows[r] or
                    num in cols[c] or
                    num in boxes[box_key]
                ):
                    return False

                # Add number into tracking sets
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_key].add(num)

        # If no duplicates were found
        return True