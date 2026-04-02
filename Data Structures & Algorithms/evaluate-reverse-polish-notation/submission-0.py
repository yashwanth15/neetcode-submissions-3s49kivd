class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for val in tokens:
            if val == "+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif val == "-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif val == "*":
                a=stack.pop()
                b=stack.pop()
                stack.append(a*b)
            elif val == "/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(val))
        return stack[0]

        