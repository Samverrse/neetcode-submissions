class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count=nums.count(nums[i])
            if count>len(nums)//2:
                return nums[i]
        