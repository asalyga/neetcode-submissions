class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, ans = 0, 0
        seen_chars = set()
        for right in range(len(s)):
            while s[right] in seen_chars:
                seen_chars.remove(s[left])
                left += 1
            seen_chars.add(s[right])
            ans = max(ans, right - left + 1)
        return ans