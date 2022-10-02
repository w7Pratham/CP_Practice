class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = -50000
        R = len(grid)
        C = len(grid[0])
        
        if(R < 3 or C < 3):
            return
        for i in range(0, R-2):
            for j in range(0, C-2):
                SUM = (grid[i][j] + grid[i][j + 1] + grid[i][j + 2]) + (grid[i + 1][j + 1]) + (grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2])
        
                if(SUM > max_sum):
                    max_sum = SUM
                else:
                    continue
        return max_sum
