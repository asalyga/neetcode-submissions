class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            first = nums[i]
            second = nums[i + 1]
            if not (first % 2 == 0 and second % 2 != 0) and not (
                second % 2 == 0 and first % 2 != 0
            ):
                return False
        return True
