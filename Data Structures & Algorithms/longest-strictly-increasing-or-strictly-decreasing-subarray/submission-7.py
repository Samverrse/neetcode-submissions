class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        temp=1
        main=0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                temp+=1
                print(temp)
            elif nums[i]>nums[i+1]:
                temp+=1
            else:
                temp=1
            main=max(temp,main)
        return main


        