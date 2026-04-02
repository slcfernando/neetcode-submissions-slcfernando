class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # track digits in each row
        rows = {r: set() for r in range(9)}

        # track digits in each column
        cols = {c: set() for c in range(9)}

        # track digits in each column
        # (r, c) here is the actual row or column divided by 3, floored
        boxes = {(r, c): set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                
                # ignore blank cells
                if n == '.':
                    continue

                # if present in a row, column, or box already, then invalid
                if (n in rows[r] or
                    n in cols[c] or
                    n in boxes[(r // 3, c // 3)]):
                    return False
                
                # add to hash sets of rows, cols, and boxes
                rows[r].add(n)
                cols[c].add(n)
                boxes[(r // 3, c // 3)].add(n)
        
        return True
