class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
            i+=1
        return nums
