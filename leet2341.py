class Solution:
    def numberOfPairs(self, nums):
        res = []
        dit = {}
        pairs = 0
        for i in nums:
            if i in dit:
                dit[i] += 1
                if not dit[i]%2:
                    pairs += 1
            else:
                dit[i] = 1
        res.append(pairs)
        res.append(len(nums)-pairs*2)
        return res

a = Solution()
print(a.numberOfPairs([1,3,2,1,3,2,2]))
