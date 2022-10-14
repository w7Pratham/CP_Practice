class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        dp = matrix[0]
        
        for row in matrix[1:]:
            dp.pop()
            dp.insert(0,row[0])
            if dp != row:
                return False
              
        return True
      
