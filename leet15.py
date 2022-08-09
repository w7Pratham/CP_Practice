class Solution:
    def twoSum(self, nums, target):
        j = -1
        while True:
            if nums[j]>target:
                j -= 1
            else:
                sec = target - nums[j]
                if sec in nums:
                    return [nums.index(sec), len(nums)+j]
                else:
                    j -= 1

a = Solution()
print(a.twoSum([-1,-2,-3,-4,-5],-8))