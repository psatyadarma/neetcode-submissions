class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        substr = set()
        l = 0
        maxLength = 0
        for r in range(len(s)):
            char = s[r]
            while char in substr:
                print(f"r is {r}, l is {l}")
                substr.remove(s[l])
                l += 1
            substr.add(char)
            r += 1
            maxLength = max(maxLength, r - l)
            print(substr)
        return maxLength