class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans=[]
        for num in nums:
            if num not in ans:
                ans.append(num)
            else:
                return True
        return False


            