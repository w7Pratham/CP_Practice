from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n):
        c = Counter([int(i) for i in str(n)])

        n,i = 0,0
        while n <= 10**9:
            n = 2**i
            d = Counter([int(n) for i in str(n)])
            if c == d: return True
            i += 1
        return False

a = Solution()
print(a.reorderedPowerOf2(40))