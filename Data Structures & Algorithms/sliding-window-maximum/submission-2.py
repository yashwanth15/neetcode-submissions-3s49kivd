from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #monotonically decreasing queue
        q=deque() #store indices
        res=[]

        for i in range(len(nums)):
            # pop elements from left if outside window
            while q and q[0] <= i-k:
                q.popleft()

            # pop elements which are less than the current element (monotonically decreasing queue)
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            
            # add the current element
            q.append(i)
            if i>=k-1:
                res.append(nums[q[0]])
        return res



            
            