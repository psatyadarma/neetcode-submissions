class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[i]:
                return False
            char = board[row][col]
            board[row][col] = '#'

            found = (
                dfs(row + 1, col, i + 1) or
                dfs(row - 1, col, i + 1) or
                dfs(row, col + 1, i + 1) or 
                dfs(row, col - 1, i + 1)
            )

            board[row][col] = char

            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False