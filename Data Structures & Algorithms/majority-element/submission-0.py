import operator
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_count = {}

        for i in range(len(nums)):
            element = elements_count.get(nums[i], 0)
            element += 1
            elements_count[nums[i]] = element

        return max(elements_count.items(), key=operator.itemgetter(1))[0]
