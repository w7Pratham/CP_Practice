class Solution:
    def insert(self,intervals,newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])
        return output

a = Solution()
print(a.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
