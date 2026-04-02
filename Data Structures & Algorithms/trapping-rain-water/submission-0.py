class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n
        res=0
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i+1])
        for i in range(n):
            if min(leftmax[i],rightmax[i])>height[i]:
                res+=min(leftmax[i],rightmax[i])-height[i]
        return res

        