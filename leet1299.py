class Solution:
    def replaceElements(self, arr):
        res = [-1]
        for i in arr[:0:-1]:
            if res[-1] > i:
                res.append(res[-1])
            else:
                res.append(i)
        return res

a = Solution()
print(a.replaceElements ([17,18,5,4,6,1]))
