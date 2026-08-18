class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp=1
        main=0
        for i in range(1,len(nums)):
            if len(nums)>1:
                temp*=nums[i]
            else:
                temp=1
            main=max(temp,main)
            print(main)
        return main

        
        
        