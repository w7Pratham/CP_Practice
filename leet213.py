class Solution:
    def rob(self, nums: List[int]) -> int:
        def fut(arr):
            r1, r2 = 0, 0
            for i in arr:
                rob_n = max(r1+i,r2)
                r1 = r2
                r2 = rob_n
            return r2
        return max(nums[0],fut(nums[1:]),fut(nums[:-1]))
