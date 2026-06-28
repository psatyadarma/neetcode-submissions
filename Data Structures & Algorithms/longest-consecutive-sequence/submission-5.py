class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        sets = set(nums)
        for i in sets:
            if i-1 not in sets:
                length = 1
                while i+1 in sets:
                    length += 1
                    i += 1
                max_length = max(max_length, length)
        return max_length
