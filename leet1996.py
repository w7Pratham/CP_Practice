class Solution():
    def numberOfWeakCharacter(self, properties):
        properties.sort()
        properties.sort(key=lambda x: -x[0])
        res = 0
        max = 0
        for atk,den in properties:
            if den<max:
                res += 1
            else:
                max = den
        return res


a = Solution()
print(a.numberOfWeakCharacter([[5,5],[6,3],[3,6]]))
print(a.numberOfWeakCharacter([[1,5],[10,4],[4,3]]))
print(a.numberOfWeakCharacter([[2,2],[3,3]]))
