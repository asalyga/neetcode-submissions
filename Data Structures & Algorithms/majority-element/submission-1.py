import operator
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_count = {}

        for i in range(len(nums)):
            elements_count[nums[i]] = elements_count.get(nums[i], 0) + 1

        return max(elements_count.items(), key=operator.itemgetter(1))[0]
