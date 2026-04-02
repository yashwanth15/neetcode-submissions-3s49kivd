class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ensure n is the smaller array
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        
        n,m = len(nums1),len(nums2)
        half = (n+m+1)//2

        left,right = 0,n

        while left<=right:
            i=(left+right)//2
            j=half-i

            left1=nums1[i-1] if i>0 else float("-inf")
            right1=nums1[i] if i<n else float("inf")

            left2=nums2[j-1] if j>0 else float("-inf")
            right2=nums2[j] if j<m else float("inf")

            if left1<=right2 and left2<=right1:
                # found the right partition
                if (n+m)%2==0:
                    return (max(left1,left2) + min(right1,right2))/2.0
                else:
                    return float(max(left1,left2))
            
            elif left1>right2:
                # too many elements in nums1 left half
                right=i-1
            else:
                # too few elements in nums1 left half
                left=i+1
        