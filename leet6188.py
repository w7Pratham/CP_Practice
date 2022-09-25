class Solution():
    def sortPeople(self,names,heights):
        ziped = list(zip(names,heights))
        ziped.sort(key=lambda x:-x[1])
        res = [i for i,j in ziped]
        return res

a = Solution()
print(a.sortPeople(["Alice","Bob","Bob"],[155,185,150]))
