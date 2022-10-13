class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dit = defaultdict(list)
        res = []

        for val,cnt in Counter(nums).items():
            dit[cnt].append(val)
        
        for cnt, vals in sorted(dit.items()):
            for v in sorted(vals,reverse = True):
                res.extend([v]*cnt)

        return res
