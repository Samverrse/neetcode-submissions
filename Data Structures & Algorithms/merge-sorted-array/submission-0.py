class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        del nums1[m:]
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        

