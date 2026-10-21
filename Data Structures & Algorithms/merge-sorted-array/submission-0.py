class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m
        r = 0
        while l < len(nums1) and r < n:
            nums1[l] = nums2[r]
            l += 1
            r+= 1
        nums1.sort()
