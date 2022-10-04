class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dit = {}
        count = 0
        for i in nums:
            if i in dit:
                count += dit[i]
                dit[i] += 1
            else:
                dit[i] = 1
        return count
