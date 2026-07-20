class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mylist=[1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    mylist[i]=max(mylist[i],1+mylist[j])
        return max(mylist)
        