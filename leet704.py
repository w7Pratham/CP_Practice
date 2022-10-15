class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = 0
        s = len(nums)-1
        while n <= s:
            mid = (n + s)//2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                s = mid - 1
            else:
                n = mid + 1 
        return -1
