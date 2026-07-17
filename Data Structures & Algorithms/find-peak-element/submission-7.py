class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       numst=sorted(nums)
       target=max(numst)
       left,right=0,len(numst)-1
       while left<=right:
        mid=(left+right)//2
        if numst[mid]==target:
            return mid
        elif numst[mid]<target:
            left=mid+1
        else:
            right=mid-1
        return -1
                
        