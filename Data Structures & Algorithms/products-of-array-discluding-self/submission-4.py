class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            tot=nums[:i]+nums[i+1:]
            prod=1
            for a in tot:
                prod*=a
            ans.append(prod)
        return ans        













        