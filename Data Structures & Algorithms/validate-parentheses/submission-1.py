class Solution:
    def isValid(self, s: str) -> bool:
        pairs={')':'(','}':'{',']':'['}
        stack=[]
        for val in s:
            if val in pairs:
                if stack and stack[-1]==pairs[val]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(val)
        if not stack:
            return True
        else:
            return False
                
                
        