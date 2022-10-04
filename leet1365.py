class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dit = {}
        cac = sorted(nums.copy())
        res = []
        
        for i in range(len(cac)):
            if cac[i] not in dit:
                dit[cac[i]] = i
        
        for i in nums:
            res.append(dit[i])
        
        return res
