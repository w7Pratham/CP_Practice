class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0 for _ in range(len(indices))]
        
        for i,j in enumerate(indices):
            res[j] = s[i]
        
        return "".join(res)
