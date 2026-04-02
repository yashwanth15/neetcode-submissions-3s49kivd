from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]+=1
        
        min_heap=[]
        for num,freq in freq_map.items():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap) # pop min freq element
        
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(min_heap)[1])
        return result
        
