class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        limit = max(a,b)
        count = 0
        for i in range(1,limit+1):
            a_in = a%i
            b_in = b%i
            if (not a_in) and (not b_in):
                count += 1
        return count
