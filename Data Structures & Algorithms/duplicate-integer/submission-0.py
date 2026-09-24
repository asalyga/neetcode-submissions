class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_table = set()
        for value in nums:
            if value in seen_table:
                return True
            seen_table.add(value)
        return False
