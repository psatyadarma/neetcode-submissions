class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-n for n in nums]
        heapq.heapify(neg)

        res = 0
        for i in range(k):
            res = -heapq.heappop(neg)
        return res