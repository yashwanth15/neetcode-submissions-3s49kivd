class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        # add 0 to heights to pop and force caluclate all the bars
        heights.append(0)
        res=0

        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                maxheight=heights[stack.pop()]
                width=i if not stack else i-stack[-1]-1
                res=max(res,maxheight*width)
            stack.append(i)
        return res
        