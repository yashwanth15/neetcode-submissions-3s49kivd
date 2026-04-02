class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=[[] for _ in range(len(nums)+1)]
        counter=defaultdict(int)
        result=[]
        for num in nums:
            counter[num]+=1
        for num,count in counter.items():
            freq[count].append(num)
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                result.append(num)
                if len(result)==k:
                    return result
        
