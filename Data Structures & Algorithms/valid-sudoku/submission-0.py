class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)      # rows[r]
        cols = defaultdict(set)      # cols[c]
        boxes = defaultdict(set)     # boxes[(br, bc)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue

                box = (r // 3, c // 3)
                if digit in rows[r] or digit in cols[c] or digit in boxes[box]:
                    return False # seen before in this row, column or box

                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)

        return True