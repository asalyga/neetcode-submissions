class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        hash_set = set(nums)
        if not hash_set:
            return 0

        for number in hash_set:
            if number - 1 not in hash_set:
                count = 1
                while number+1 in hash_set:
                    count += 1
                    number +=1
                max_count = max(count, max_count)
        return max_count
