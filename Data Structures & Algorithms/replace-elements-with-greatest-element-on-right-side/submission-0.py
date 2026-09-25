class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for left_idx in range(len(arr)):
            highest_right_idx = left_idx+1
            for right_idx in range(left_idx+1, len(arr)):
                if arr[right_idx] > arr[highest_right_idx]:
                    highest_right_idx = right_idx
                arr[left_idx] = arr[highest_right_idx]
        arr[-1] = -1
        return arr