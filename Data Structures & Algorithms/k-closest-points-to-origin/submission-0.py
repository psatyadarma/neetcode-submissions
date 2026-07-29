class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            distance = -(point[0]**2+point[1]**2)
            heapq.heappush(maxHeap, [distance, point[0], point[1]])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        return res