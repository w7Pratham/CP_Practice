class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nsum = 0
        msum = nums[0]
        for i in range(len(nums)):
            nsum += nums[i]
            msum = max(nsum,msum)
            if nsum < 0:
                nsum = 0
        return(msum)
            
