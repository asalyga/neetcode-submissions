class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest_val = -1
        for i in reversed(range(len(arr))):
            old_val = arr[i]
            arr[i] = highest_val
            if old_val > highest_val:
                highest_val = old_val
            print(f"Arr is {arr}")
        return arr