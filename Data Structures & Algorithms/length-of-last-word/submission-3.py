class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right_index = len(s) - 1
        char_count = 0
        while right_index >= 0:
            if not s[right_index].isalpha() and char_count == 0:
                right_index -= 1
            elif not s[right_index].isalpha() and char_count > 0:
                return char_count
            else:
                 char_count +=1
                 right_index -=1
        return char_count
