class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        res = []
        dit = sorted(Counter(words).items())
        for val,cnt in sorted(dit,key = lambda x:x[1], reverse = True):
            res.append(val)
            k -= 1
            if not k:
                break
        return res
