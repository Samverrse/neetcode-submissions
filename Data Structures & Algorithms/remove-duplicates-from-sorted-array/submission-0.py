class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans=[]
        for num in nums:
            if num not in ans:
                ans.append(num)
            nums[:len(ans)]=ans
        return len(ans)
        

        