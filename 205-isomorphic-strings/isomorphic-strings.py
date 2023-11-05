class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping_s_t = {}
        mapping_t_s = {}

        for i in range(len(s)):
            if s[i] in mapping_s_t:
                if mapping_s_t[s[i]] != t[i]:
                    return False
            else:
                mapping_s_t[s[i]] = t[i]

            if t[i] in mapping_t_s:
                if mapping_t_s[t[i]] != s[i]:
                    return False
            else:
                mapping_t_s[t[i]] = s[i]

        return True        