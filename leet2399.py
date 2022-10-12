class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        dit = {}
        
        for index, char in enumerate(s):
            if char not in dit:
                dit[char] = index + 1
            else:
                dit[char] = abs(dit[char] - index)
                
        alpha = "abcdefghijklmnopqrstuvwxyz"
        
        for dist, alpha in zip(distance,list(alpha)):
            if alpha in dit and dist != dit[alpha]:
                return False
            
        return True
