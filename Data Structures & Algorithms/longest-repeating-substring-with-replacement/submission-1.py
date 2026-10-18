class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        left = 0
        max_freq = 0
        ans = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            window_length = right - left + 1
            replacements_needed = window_length - max_freq

            while replacements_needed > k:
                counts[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                replacements_needed = window_length - max_freq

            ans = max(ans, right - left + 1)

        return ans