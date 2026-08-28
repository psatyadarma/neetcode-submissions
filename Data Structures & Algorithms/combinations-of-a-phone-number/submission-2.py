class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(letters, idx):
            if idx == len(digits):
                res.append(letters)
                return
            for char in phone[digits[idx]]:
                backtrack(letters + char, idx+1)
        backtrack("",0)
        return res
            


