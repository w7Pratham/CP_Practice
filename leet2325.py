class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dit = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        cur = 0
        for i in key:
            if i not in dit and i != " ":
                dit[i] = alpha[cur]
                cur += 1
        res = []
        for i in message:
            if i == " ":
                res.append(i)
            else:
                res.append(dit[i])
        return "".join(res)
