class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightPointer=len(nums)-1
        result=[]
        prefix=[1]*(rightPointer+1)
        postfix=[1]*(rightPointer+1)
        postfix[rightPointer]=1
        for i,num in enumerate(nums):
            print(i,num)
            if i>0:
                prefix[i]=prefix[i-1]*nums[i-1]
        for i in range(rightPointer,-1,-1):
            if i<rightPointer:
                postfix[i]=postfix[i+1]*nums[i+1]
        for i in range(rightPointer+1):
            result.append(prefix[i]*postfix[i])
        return result
        
        