class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = []
        shorter_range = min(len(word1), len(word2))
        for i in range(shorter_range):
            word3.append(word1[i])
            word3.append(word2[i])

        if len(word1) > len(word2):
            word3.append(word1[shorter_range:])
        else:
            word3.append(word2[shorter_range:])
        return "".join(word3)
