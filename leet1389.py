class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for i in range(len(index)):
            if index[i] + 1 <= len(res):

                res.append(0)
                cur = 0
                for j in range(len(res) - 2, index[i] - 1, -1):
                    res[j + 1] = res[j]
                    cur = j
                res[cur] = nums[i]

            else:
                res.append(nums[i])

        return res
