class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        char_length = len(strs[0])
        first_word_letters = strs[0]
        for i in range(1, len(strs)):
            curr_char_length = 0
            for j in range(len(strs[i])):
                if j > len(strs[0]) - 1:
                    break
                if strs[i][j] == first_word_letters[j] and j <= len(strs[0]):
                    curr_char_length += 1
                else:
                    break
                
            char_length = min(char_length, curr_char_length)
        return str(first_word_letters[:char_length])
