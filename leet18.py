class Solution:
    def fourSum(self,nums,target):
        #if len(nums)<4:
            #return []
        nums.sort()
        res = []
        a,b = 0,len(nums)-1
        for i in nums:
            l,r = a+1,b-1
            while l<r:
                fsum = nums[a] + nums[l] + nums[r] + nums[b]
                if fsum > target:
                    r -= 1
                elif fsum < target:
                    l += 1
                else:
                    if [nums[a], nums[l], nums[r], nums[b]] not in res:
                        res.append([nums[a], nums[l], nums[r], nums[b]])
                    l += 1
            if fsum>target:
                b-=1
            else:
                a+=1
        return res

eg = Solution()
print(eg.fourSum([-3,-1,0,2,4,5],2))
