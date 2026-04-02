class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotoniqally decreasing stack
        res=[0]*len(temperatures)
        mono=[]
        for i in range(len(temperatures)-1,-1,-1):
            while mono and temperatures[mono[-1]]<=temperatures[i]:
                mono.pop()
            if mono:
                res[i]=mono[-1]-i
            mono.append(i)
        return res
        