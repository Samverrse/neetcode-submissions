class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        while len(nums)>k:
            nums.pop()
        return min(nums)        