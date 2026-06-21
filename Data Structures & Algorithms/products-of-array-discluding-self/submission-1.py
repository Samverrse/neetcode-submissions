class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans=[]
        for i in range (len(nums)):
            a=nums[:i]+nums[i+1:]
            prod=1
            for x in a: 
                prod*=x
            ans.append(prod)
        return ans
        













        