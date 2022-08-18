from collections import Counter
class Solution:
    def minSetSize(self,arr):
        res = 0
        ln,set_sum = len(arr),0
        for j in sorted(Counter(arr).values(), reverse = True):
            if set_sum<ln/2:
                set_sum += j
                res += 1
        return res

a = Solution()
print(a.minSetSize([1,2,3,4,5,6,7,8,9,10]))
print(a.minSetSize([7,7,7,7,7,7]))
print(a.minSetSize([5,5,5,2,7,3,3,3,3]))
# print(a.generateMatrix())
# print(a.generateMatrix())