class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range (len(nums)):
            sum=nums[:i]+nums[i+1:]
            prod=1
            for x in sum:
                prod*=x
            ans.append(prod)
        return ans

        













        