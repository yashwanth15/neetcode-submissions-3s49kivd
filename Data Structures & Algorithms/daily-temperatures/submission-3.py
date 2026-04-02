class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotoniqally decreasing stack
        n=len(temperatures)
        res=[0]*n
        mono=[]
        for i in range(n):
            while mono and temperatures[i]>temperatures[mono[-1]]:
                prev=mono.pop()
                res[prev]=i-prev
            mono.append(i)
        return res
        