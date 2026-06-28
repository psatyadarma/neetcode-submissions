class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic_s = {}
        for i in s:
            if i in dic_s:
                dic_s[i] += 1
            else:
                dic_s[i] = 1
        dic_t = {}
        for i in t:
            if i in dic_t:
                dic_t[i] += 1
            else:
                dic_t[i] = 1
        for i in dic_s:
            if i not in dic_t:
                return False
            if dic_s[i] != dic_t[i]:
                return False
        return True