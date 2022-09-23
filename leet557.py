class Solution():
    def reverseWords(self,s):
        rev = s.split()
        res = []
        for i in rev:
            res.append(i[::-1])
        return " ".join(res)

a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))
