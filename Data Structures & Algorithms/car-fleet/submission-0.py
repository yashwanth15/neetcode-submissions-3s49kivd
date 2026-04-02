class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair position and speed and sort by position in descending order
        cars=sorted(zip(position,speed),reverse=True)
        stack=[]
        #use monotoniqally increasing stack to track fleet times
        #only if car time is more than previous fleet add it to stack
        #cars with same or less time become part of the fleet.
        for pos,spd in cars:
            time=(target-pos)/spd
            if not stack or time>stack[-1]:
                stack.append(time)
            
        return len(stack)
        