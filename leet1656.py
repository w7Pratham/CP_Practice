class OrderedStream:

    def __init__(self, n: int):
        self.seen = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        seen, ptr = self.seen, self.ptr
        
        seen[idKey] = value
        res = []
        while ptr in seen:
            res.append(seen[ptr])
            del seen[ptr]
            ptr += 1
        
        self.ptr = ptr
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
