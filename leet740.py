class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums = sorted(Counter(nums).items())
        earn_1, earn_2  = 0, 0
        for i in range(len(nums)):
            new_earn = nums[i][0]*nums[i][1]
            if i > 0 and nums[i][0] == nums[i-1][0] + 1:
                earn_1, earn_2 = earn_2, max(earn_2,new_earn + earn_1)
            else:
                earn_1, earn_2 = earn_2 , new_earn + earn_2
        return earn_2
            
