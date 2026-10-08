class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word_letters = strs[0]
        for i in range(len(first_word_letters)):
            for word in strs[1:]:
                if i >= len(word) or word[i] != first_word_letters[i]:
                    return first_word_letters[:i]
        return first_word_letters
