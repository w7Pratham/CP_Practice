class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        return all(i%2 == 0 for i in Counter(nums).values())
