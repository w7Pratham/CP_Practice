class Solution:
    def prefixCount(self, words,pref):
        count = 0

        for i in words:
            if i[:len(pref)] == pref:
                count += 1
        return count

a = Solution()
print(a.prefixCount(["pay","attention","practice","attend"],"at"))
