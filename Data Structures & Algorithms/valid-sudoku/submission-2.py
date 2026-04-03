class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = [set() for _ in range(9)]
        col_hash = [set() for _ in range(9)]
        box_hash = {(r, c) : set() for r in range(3) for c in range(3)}

        for row in range(9):
            for col in range(9):
                n = board[row][col]
                if n == '.':
                    continue

                if (n in row_hash[row] or
                    n in col_hash[col] or
                    n in box_hash[(row // 3, col // 3)]):
                    return False

                row_hash[row].add(n)
                col_hash[col].add(n)
                box_hash[(row // 3, col // 3)].add(n)
        
        return True