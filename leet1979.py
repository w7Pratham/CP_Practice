class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def GCD(x,y):
            while (y):
                x, y = y, x % y
            return abs(x)
        
        return GCD(min(nums),max(nums))
