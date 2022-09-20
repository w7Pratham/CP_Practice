class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = "{0:032b}".format(n)
        rev_n = bin_n[::-1]
        return int(rev_n,2)
