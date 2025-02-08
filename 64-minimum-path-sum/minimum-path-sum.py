class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Fill first row (can only come from the left)
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        # Fill first column (can only come from above)
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        # Fill rest of the grid (minimum of top or left path)
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        return grid[-1][-1]