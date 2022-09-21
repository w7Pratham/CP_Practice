class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        counter = collections.Counter(n)
        return counter.get("1", 0)
