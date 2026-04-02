class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        l=r=0
        q=collections.deque()
        while r<len(nums):
            # step1: Remove elements smaller than current from back
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            
            # step2: Remove elements outside the window from front
            if q and q[0]<l:
                q.popleft()
            
            # step3: Add current index to deque
            q.append(r)
            
            # step4: When window size ≥ k, record front value as it's the max value in the window
            if r>=k-1:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output

        