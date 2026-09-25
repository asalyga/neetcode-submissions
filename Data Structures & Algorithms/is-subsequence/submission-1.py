class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_pointer = 0
        s_pointer = 0
        while s_pointer != len(s) and t_pointer != len(t):
            current_char = s[s_pointer]

            if t[t_pointer] == current_char:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == len(s)
