class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = [0]
        mini = prices[0]
        maxi = prices[0]
        for i in prices:
            if i<mini:
                mini = i
                maxi = i
            if i>maxi:
                maxi = i
            if maxi-mini>0:
                res.append(maxi-mini)
        return max(res)
