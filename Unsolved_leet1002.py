from collections import Counter
class Solution:
    def commonChars(self, words):
        res = []
        dp = []
        temp = list(words[0])
        for i in words[1:len(words)]:
            for val, cnt in list(Counter(i).items()):
                if val in temp:
                    res.extend([val]*min(temp.count(val), cnt))
            
        return res

a = Solution()
print(a.commonChars(["cool","lock","cook"]))

"""
want to iterate over res for first ```for loop``` for every element in words.
"""
