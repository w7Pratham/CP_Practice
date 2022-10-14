class Solution:
    def fib(self, n: int) -> int:
        if not n: return 0
        
        seq = [0,1]
        for _ in range(1,n):
            seq.append(sum(seq))
            seq.pop(0)
            
        return seq[1]
