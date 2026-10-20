class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        shorter_range = min(len(word1), len(word2))
        for i in range(shorter_range):
            word3 += word1[i]
            word3 += word2[i]

        word3 += word1[shorter_range:] if len(word1) > len(word2) else word2[shorter_range:]
        return word3
