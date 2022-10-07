class Solution:
    def finalPrices(self, prices):
        stack = []

        for i, num in enumerate(prices):
            while stack and prices[stack[-1]] >= num:
                popIndex = stack.pop()
                prices[popIndex] -= num
            stack.append(i)
        return prices

a = Solution()
print(a.finalPrices([8,4,6,2,3]))
