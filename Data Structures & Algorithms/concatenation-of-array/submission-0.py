class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answ = [0 for n in range(len(nums)*2)]

        for idx in range(len(nums)):
            answ[idx] = nums[idx]
            answ[idx+len(nums)] = nums[idx] 
            
        return answ