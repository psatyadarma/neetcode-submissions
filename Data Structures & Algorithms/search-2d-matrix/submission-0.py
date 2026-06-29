class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l <= r:
            mid = l + (r-l)//2
            mid_row = mid // cols
            mid_col = mid % cols
            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False