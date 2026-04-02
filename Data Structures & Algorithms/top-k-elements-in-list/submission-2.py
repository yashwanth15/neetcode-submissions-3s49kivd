class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniqueMap=defaultdict(int)
        finalResult=[]
        for i,element in enumerate(nums):
            uniqueMap[element]+=1
        sorted_map=sorted(uniqueMap.items(), key=lambda kv:kv[1], reverse=True)
        j=0
        for i in sorted_map:
            if j==k:
                break
            finalResult.append(i[0])
            j+=1
        return finalResult