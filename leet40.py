class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        if sum(candidates) < target: return []
        res = []
        def dfs(i,cur,total):
            if total == target:
                if cur.copy() not in res: res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res

a = Solution()
print(a.combinationSum2([10,1,2,7,6,1,5],8))