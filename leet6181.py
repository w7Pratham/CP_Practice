class Solution():
    def longestContinuousSubstring(self,s):
        res = 0
        alphas = "abcdefghijklmnopqrstuvwxyz"
        res_str = ""
        for i in s:
            if res_str + i in alphas:
                res_str = res_str + i
                res = max(res, len(res_str))
            else:
                res_str = i
        return res

a = Solution()
# print(a.longestContinuousSubstring("abacaba"))
print(a.longestContinuousSubstring("abcde"))
