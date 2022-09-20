class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nset = set(nums)
        max_nums = [(nums.count(i),i) for i in nset]
        max_nums.sort(reverse = True)
        return max_nums[0][1]
