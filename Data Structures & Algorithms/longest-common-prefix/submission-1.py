class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char_length = len(strs[0])
        first_word_letters = strs[0]
        for i in range(1, len(strs)):
            curr_char_length = 0
            for j in range(min(len(strs[0]), len(strs[i]))):
                if not strs[i][j] == first_word_letters[j]:
                    break
                curr_char_length += 1
            char_length = min(char_length, curr_char_length)
        return str(first_word_letters[:char_length])
