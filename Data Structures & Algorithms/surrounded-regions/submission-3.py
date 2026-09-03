class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for c in range(cols):
            for r in (0, rows-1):
                if board[r][c] == 'O':
                    board[r][c] = '#'
        
        for c in (0, cols - 1):
            for r in range(rows):
                if board[r][c] == 'O':
                    board[r][c] = '#'
        queue = deque()
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    queue.append((r,c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    queue.append((nr,nc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '#':
                    board[r][c] = 'O'
            