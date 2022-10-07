class Solution:
    def oddCells(self, m, n, indices):
        cac = [[0 for _ in range(n)] for _ in range(m)]
        count = 0

        for r,c in indices:
            for i in range(n):
                cac[r][i] += 1
            for j in range(m):
                cac[j][c] += 1

        for i in range(m):
            for j in range(n):
                if cac[i][j]%2:
                    count += 1

        return count

a = Solution()
print(a.oddCells(2,3,[[0,1],[1,1]]))
