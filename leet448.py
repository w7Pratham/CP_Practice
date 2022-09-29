class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        allNums = [0] * len(nums)
        for i in nums:
            allNums[i - 1] = i

        return [i + 1 for i in range(len(allNums)) if allNums[i] == 0]
