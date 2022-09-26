class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dit = {}
        for i,j in enumerate(nums):
            if j in dit and i-dit[j]<=k:
                return True
            dit[j] = j
        return False
