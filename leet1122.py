class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        dit = defaultdict(int)
        
        for i in arr1:
            dit[i] += 1
        
        for j in arr2:
            res.extend([j]*dit[j])
        
        for k in sorted(list(set(arr1) - set(arr2))):
            res.extend([k]*dit[k])
        
        return res
