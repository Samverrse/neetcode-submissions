class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-k):
            if nums[i]==nums[i+k]:
                return True
        return False