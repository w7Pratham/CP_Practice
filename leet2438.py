class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [1]
        while sum(powers) < n:
            powers.append(powers[-1]*2)

        temp = []
        if sum(powers) > n:
            for i in powers[::-1]:
                temp.append(i)
                if sum(temp) > n:
                    temp.pop()
                    continue
            powers = sorted(temp)
        res = []
        for l, r in queries:
            cac = 1
            for i in powers[l:r+1]:
                cac *= i
            res.append(cac%(10**9 + 7))
        return res
