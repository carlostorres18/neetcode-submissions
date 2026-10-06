class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_str = "".join(sorted(s))
        t_str = "".join(sorted(t))
        return s_str == t_str