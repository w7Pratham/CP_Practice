class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first,]
        
        for i in range(len(encoded)):
            res.append(res[i] ^ encoded[i])
        
        return res
