class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            # Check rows
        for i in range(9):
            seen = set()

            for j in range(9):
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])

        # Check columns
        for i in range(9):
            seen = set()

            for j in range(9):
                if board[j][i] == ".":
                    continue

                if board[j][i] in seen:
                    return False

                seen.add(board[j][i])

        # Check 3x3 boxes
        for row_start in range(0, 9, 3):
            for col_start in range(0, 9, 3):
                seen = set()

                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in seen:
                            return False

                        seen.add(board[i][j])

        return True