class Solution:
    def nextPermutation(self,nums):
        nums = nums
        ln = len(nums)
        sw = ln - 1
        brk = ln - 2
        #for i in range(brk,-1,-1):
        while brk >= 0:
            if nums[brk] < nums[brk+1]:
                break
            brk -= 1
        if brk<0:
            nums.reverse()
            #return

        else:
            while sw>brk:
                if nums[sw]>nums[brk]:
                    break
                sw -= 1
            nums[sw],nums[brk]=nums[brk],nums[sw]
            l,r = brk+1,ln-1
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1 ; r -= 1


a = Solution()
nums = [3,2,1]
a.nextPermutation(nums)
print(nums)