class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        main=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==nums[i-1]+1:
                count+=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                count=1
            main=max(count,main)
        return main
                    