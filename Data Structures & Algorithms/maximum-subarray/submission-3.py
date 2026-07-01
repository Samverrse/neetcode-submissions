class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=0
        main=0
        for num in nums:
            if temp>=0:
                temp+=num
            else:
                temp=num
            main=max(temp,main)
        return main






        