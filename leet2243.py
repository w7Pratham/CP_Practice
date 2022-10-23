class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            catch_s = [s[i:i+k] for i in range(0,len(s),k)]
            s = ""
            for i in catch_s:
                s += str(sum(list(map(int, list(i)))))
        return s
