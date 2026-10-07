class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for num in nums:
            x[num] = x.get(num, 0) + 1
        
        count_table = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
        return_arr = []
        keys_list = list(count_table.keys())
        for i in range(k):
            return_arr.append(keys_list[i])
        return return_arr

        