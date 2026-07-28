class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            s3 = abs(s1-s2)
            if s3 > 0:
                heapq.heappush(stones, -s3)
        return -stones[0] if stones else 0