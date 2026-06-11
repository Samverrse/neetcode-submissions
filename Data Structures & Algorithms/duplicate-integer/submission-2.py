class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final=[]
        for num in nums:
            if num in final:
                return True
            final.append(num)
        return False    