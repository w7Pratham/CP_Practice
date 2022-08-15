class Solution:
    def countAndSay(self,n):
        if n == 1: return "1"
        if n == 2: return "11"

        t = "11"
        for _ in range(n-2):
            c = 1
            res = ""
            t = t + "_"
            for i in range(len(t) - 1):
                if t[i] == t[i + 1]:
                    c += 1
                    continue
                res = res + str(c) + t[i]
                c = 1
            t = res
        return t





a = Solution()
eg = a.countAndSay(6)
print(eg)