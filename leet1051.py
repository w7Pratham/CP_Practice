class Solution:
    def heightChecker(self, heights):
        cac = sorted(heights.copy())
        count = 0

        for i, j in zip(cac, heights):
            if i != j:
                count += 1
        return count

a = Solution()
print(a.heightChecker([1,1,4,2,1,3]))
