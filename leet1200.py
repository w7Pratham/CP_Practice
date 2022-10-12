class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        dit = {}
        min_dit = float('inf')
        
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] not in dit:
                dit[arr[i+1]-arr[i]] = [[arr[i],arr[i+1]]]
                
            else:
                dit[arr[i+1]-arr[i]].append([arr[i],arr[i+1]])
                
            if arr[i+1]-arr[i] < min_dit:
                min_dit = arr[i+1]-arr[i]
                
        return list(dit[min_dit])
