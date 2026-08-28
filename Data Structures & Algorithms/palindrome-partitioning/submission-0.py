class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def backtrack(start):
            if start == len(s):
                res.append(path.copy())
                return
            # try every substring starting at start
            for end in range(start,len(s)):
                substring = s[start:end+1]
                
                # check if palindrome
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end+1)
                    path.pop()
        backtrack(0)
        return res
