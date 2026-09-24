class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_table = {}
        t_table = {}
        for value in s:
            s_table[value] = s_table.get(value, 0) + 1

        for value in t:
            t_table[value] = t_table.get(value, 0) + 1
        return s_table == t_table