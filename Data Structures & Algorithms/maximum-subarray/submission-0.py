class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub=nums[0]
        tempsum=0
        for num in nums:
            if tempsum>0:
                tempsum+=num
            else:
                tempsum=num
            maxsub=max(tempsum,maxsub)
        return maxsub


        