class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-n for n in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            prev = -1*heapq.heappop(stones)
            cur = -1*heapq.heappop(stones)
            heapq.heappush(stones,-1*abs(prev-cur))
        return -1*stones[0]