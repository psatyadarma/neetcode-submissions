class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        tempMax = nums[0]
        res = tempMax

        for num in nums[1:]:
            tempMax = max(num, num*currMax, num*currMin)
            currMin = min(num, num*currMax, num*currMin)
            currMax = tempMax
            res = max(res,currMax)

        return res