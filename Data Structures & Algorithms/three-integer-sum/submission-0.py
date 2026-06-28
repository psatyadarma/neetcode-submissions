class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            first = nums[i]
            target = -1*first
            dic = {}
            for j in range(i+1, len(nums)):
                num = nums[j]
                if num in dic:
                    # print(f"first is {first}, dic[num] is {dic[num]}, num is {num}")
                    subset = [first, dic[num], num]
                    if subset not in res:
                        # print(subset)
                        res.append(subset)
                dic[target - num] = num
        return res

