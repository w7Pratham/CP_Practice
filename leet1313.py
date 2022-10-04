class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(0,len(nums)//2):
            freq, val = nums[2*i], nums[2*i+1]
            
            res.extend([val]*freq)
            
        return res
