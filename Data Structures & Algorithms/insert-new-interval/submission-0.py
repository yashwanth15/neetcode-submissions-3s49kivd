class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        i=0
        for a,b in intervals:
            if newInterval[1]<a:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>b:
                res.append([a,b])
            else:
                newInterval=[
                    min(a,newInterval[0]),
                    max(b,newInterval[1])
                ]
            i+=1
        res.append(newInterval)
        return res
        