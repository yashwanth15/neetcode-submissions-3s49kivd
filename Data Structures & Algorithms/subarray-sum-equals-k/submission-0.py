class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_array_count=defaultdict(int)
        prefix_array_count[0]=1
        prefix_sum=0
        res=0
        for num in nums:
            prefix_sum+=num

            existing_prefix_array_sum = prefix_sum-k
            if existing_prefix_array_sum in prefix_array_count:
                res+=prefix_array_count[existing_prefix_array_sum]
            
            prefix_array_count[prefix_sum]+=1
        return res