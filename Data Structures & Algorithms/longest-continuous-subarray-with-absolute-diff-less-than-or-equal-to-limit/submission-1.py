class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq=deque() #decreasing monotonique queue
        maxq=deque() #increasing monotonique queue
        l=0
        res=0
        for r,num in enumerate(nums):
            while minq and nums[minq[-1]]>num:
                minq.pop()
            while maxq and nums[maxq[-1]]<num:
                maxq.pop()

            minq.append(r)
            maxq.append(r)

            while nums[maxq[0]]-nums[minq[0]]>limit:
                if minq[0]==l:
                    minq.popleft()
                if maxq[0]==l:
                    maxq.popleft()
                l+=1

            res=max(res,r-l+1)
        return res


        