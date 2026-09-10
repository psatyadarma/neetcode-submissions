class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob_line(houses):
            prev2, prev1 = 0,0
            for house in houses:
                curr = max(prev1, house+prev2)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(rob_line(nums[1:]),rob_line(nums[:-1]))