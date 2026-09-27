class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right_index = len(s) - 1
        char_count = 0
        while not s[right_index].isalpha():
                right_index -= 1
        while s[right_index].isalpha() and right_index >= 0:
                char_count += 1
                right_index -= 1
        return char_count
