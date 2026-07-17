class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp=nums[0]
        main=nums[0]
        for i in range(1,len(nums)):
            if temp>=0:
                temp*=nums[i]
            else:
                temp=nums[i]
            main=max(temp,main)
            print(main)
        return main

        
        
        