class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def nebor(a,b):
            return sum([1 for i in range(len(a)) if a[i]!=b[i]])==1
        q = [[start,0]]
        visited = {start}
        while q:
            cur, mutations = q.pop(0)
            if cur==end: return mutations
            for neb in bank:
                if nebor(cur,neb) and neb not in visited:
                    visited.add(neb)
                    q.append([neb,mutations+1])
        return -1
