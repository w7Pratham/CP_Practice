class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        cac = []

        for i in range(len(mat)):
            if [i, i] not in cac:
                res += mat[i][i]
                cac.append([i, i])

        for j in range(len(mat)):
            if [j, i] not in cac:
                res += mat[j][i]
                cac.append([j, i])
            i -= 1

        return res
