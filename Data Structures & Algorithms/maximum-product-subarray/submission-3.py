class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        temp=1
        main=0
        for num in nums:
            if temp>=0:
                temp*=num
            else:
                temp=num
            main=max(temp,main)
            print(main)
        return main

        
        
        