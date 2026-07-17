class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ans=[]
        ans.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                ans.append(nums[i])
                final=max(ans)
        return nums.index(final)
                
        