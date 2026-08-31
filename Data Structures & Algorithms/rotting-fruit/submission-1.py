class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        maxVal = 2
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if grid[nr][nc] != 1:
                    continue
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr,nc))
                maxVal = max(maxVal, grid[nr][nc])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return maxVal - 2        