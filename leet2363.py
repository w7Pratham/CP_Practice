class Solution:
    def mergeSimilarItems(self, items1, items2):
        dit = {}
        item = items1 + items2

        for va,wt in item:
            if va in dit:
                dit[va] += wt
            else:
                dit[va] = wt

        ls = list(dit.items())
        ls.sort(key = lambda x:x[0])
        return ls

a = Solution()
print(a.mergeSimilarItems([[1,1],[4,5],[3,8]],[[3,1],[1,5]]))
