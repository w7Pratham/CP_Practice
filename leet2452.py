class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def fut(a,b):
            ret = 0
            for i in range(len(a)):
                if a[i] != b[i]: ret += 1
            return ret
        res = []
        for q in queries:
            for d in dictionary:
                if fut(q,d) <= 2:
                    res.append(d)
                    break
        return res
