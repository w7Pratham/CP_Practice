class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        dif = arr[0] - arr[1]
        pre = arr[1]
        
        for i in arr[2:]:
            if pre - i != dif:
                return False
            pre = i
        return True
