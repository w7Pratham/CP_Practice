class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(rowIndex):
            temp = [0] + res + [0]
            row = []
            for j in range(len(res)+1):
                row.append(temp[j]+temp[j+1])
            res = row
        return res
