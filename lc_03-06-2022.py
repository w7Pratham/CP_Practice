# Range Sum Query 2D - Immutable
#https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.dp = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                left = self.dp[r][c - 1] if c else 0
                up = self.dp[r - 1][c] if r else 0
                diagonal = self.dp[r - 1][c - 1] if r and c else 0
                self.dp[r][c] = matrix[r][c] + left + up - diagonal

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        left = self.dp[r2][c1 - 1] if c1 else 0
        up = self.dp[r1 - 1][c2] if r1 else 0
        diagonal = self.dp[r1 - 1][c1 - 1] if r1 and c1 else 0
        return self.dp[r2][c2] - left - up + diagonal

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
