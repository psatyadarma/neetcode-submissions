class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()] 
        heapq.heapify(heap)
        res = 0
        while heap:
            carry, used = [], 0
            for i in range(n+1):
                if not heap:
                    break
                task = heapq.heappop(heap) + 1
                if task:
                    carry.append(task)
                used += 1
            for c in carry:
                heapq.heappush(heap,c)
            res += (n+1) if heap else used
        return res

