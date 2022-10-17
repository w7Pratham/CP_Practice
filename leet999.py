class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        bod = board[::]
        rows =  ["".join((i for i in ro if i != ".")) for ro in bod]
        cols = ["".join((i for i in list(co) if i != ".")) for co in list(zip(*bod))]
        
        rows = rows + cols
        
                
        return sum("Rp" in row for row in rows) + sum("pR" in row for row in rows)

#Simplified version of above code
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        bod = board[::]
        rows =  [[i for i in ro if i != "."] for ro in bod]
        cols = [[i for i in list(co) if i != "."]for co in list(zip(*bod))]
        
        count = 0
        rows = rows + cols
        
        for row in rows:
            if len(row) < 2:
                continue
            if "pR" in "".join(row):
                count += 1
            if "Rp" in "".join(row):
                count += 1
                
        return count
