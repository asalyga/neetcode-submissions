class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        candidate_count = 0

        for number in nums:
            if candidate_count == 0:
                candidate = number
                candidate_count += 1
            elif number == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1

        return candidate
