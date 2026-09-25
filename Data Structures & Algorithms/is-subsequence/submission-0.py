class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        last_checked_t_idx = 0
        for s_idx in range(len(s)):
            current_char = s[s_idx]
            found = False
            print(f"Current char is: {current_char}")
            for t_idx in range(last_checked_t_idx, len(t)):
                print(f"T_IDX IS {t_idx}")
                print(f"checking char in t: {t[t_idx]}")
                if current_char == t[t_idx]:
                    found=True
                    last_checked_t_idx = t_idx+1
                    break
            print(f"Was found: {found}")
            if found == False:
                return False
        return True
