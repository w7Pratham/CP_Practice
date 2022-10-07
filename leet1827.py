class Solution:
    def minOperations(self, nums):
        res = 0

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                continue
            res += nums[i] - nums[i + 1] + 1
            nums[i + 1] += nums[i] - nums[i + 1] + 1

        return res

a = Solution()
print(a.minOperations([1,1,1]))
