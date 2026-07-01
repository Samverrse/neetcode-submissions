class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        temp=0
        main=0
        nums=sorted(set(nums))
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                temp+=1
            else:
                temp=0
            main=max(temp,main)
        return main+1
                    