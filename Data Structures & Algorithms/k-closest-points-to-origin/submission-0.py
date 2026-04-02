class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        res=[]
        for x,y in points:
            distance = math.sqrt(x*x + y*y)
            heapq.heappush(dist,(distance,x,y))
        for _ in range(k):
            distance,x,y = heapq.heappop(dist)
            res.append([x,y])
        return res

        