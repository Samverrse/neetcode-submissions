class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        
        for i in range(len(nums)):
            prod=1
            new_list=nums[:i]+nums[i+1:]
            for n in new_list:
                prod*=n
            ans.append(prod)
        return ans
            











        