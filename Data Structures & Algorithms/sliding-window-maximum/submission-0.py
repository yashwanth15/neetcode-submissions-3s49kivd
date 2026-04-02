class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        l=r=0
        q=collections.deque()
        while r<len(nums):
            # pop the small elements from queue and make it an always decreasing queue
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            
            q.append(r)

            # if window moved, remove the left indices that are no longer part of the window
            if q[0]<l:
                q.popleft()
            
            if r>=k-1:
                #max value index is always at the left of the queue
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

        