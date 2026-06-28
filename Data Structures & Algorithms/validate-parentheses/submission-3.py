class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        char_dict = {')':'(', '}': '{', ']':'['}
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != char_dict[char]:
                    return False
        if stack:
            return False
        return True
