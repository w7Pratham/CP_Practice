class Solution:
    def mergeSimilarItems(self, items1, items2):
        dit = {}
        for va,wt in items1:
            if va in dit:
                dit[va] += wt
            else:
                dit[va] = wt
        for va,wt in items2:
            if va in dit:
                dit[va] += wt
            else:
                dit[va] = wt
        ls = list(dit.items())
        ls.sort(key = lambda x:x[0])
        return ls

a = Solution()
print(a.mergeSimilarItems([[1,1],[4,5],[3,8]],[[3,1],[1,5]]))
