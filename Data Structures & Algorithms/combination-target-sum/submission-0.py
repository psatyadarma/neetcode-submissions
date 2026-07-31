class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [],[]
        def backtrack(start, remaining_sum):
            if remaining_sum == 0:
                res.append(path[:])
            if remaining_sum < 0:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, remaining_sum - nums[i])
                path.pop()
        
        backtrack(0, target)
        return res