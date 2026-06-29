class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(k):
            return sum((p + k - 1)//k for p in piles)
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            k = l + (r-l)//2
            hours = calculate(k)
            if hours <= h:
                ans = k 
                r = k - 1
            else:
                l = k + 1
        return ans