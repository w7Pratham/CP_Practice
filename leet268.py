class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            try:
                if nums[i] != i:
                    return i
            except:
                return i
