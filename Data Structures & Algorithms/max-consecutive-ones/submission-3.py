class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp=0
        main=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1
            else:
                temp=0
            main=max(temp,main)
        return main                





        