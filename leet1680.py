class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1,n+1):
            cac = str(bin(i))
            res += cac[2:]
        if int(res,2) > (10**9):
            return int(res,2)%(10**9 + 7)
        else:
            return int(res,2)
