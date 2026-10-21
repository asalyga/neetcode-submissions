class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = l + 1
        k = 1
        while r < len(nums):
            if nums[r] != nums[l]:
                k += 1
                l+=1
                nums[l] = nums[r]
            r+=1
        return k