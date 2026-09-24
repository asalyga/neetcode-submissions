class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_values = {}
        for idx, value in enumerate(nums):
            to_find = target - value
            found = seen_values.get(to_find)
            if found is not None:
                return [found, idx]
            seen_values[value] = idx