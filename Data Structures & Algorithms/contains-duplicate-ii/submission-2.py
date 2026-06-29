class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        myset=set()
        l=0
        for r in range(len(nums)):
            if r-l>k:
                myset.remove(nums[l])
                l+=1
            if nums[r] in myset:
                return True
            myset.add(nums[r])
        return False