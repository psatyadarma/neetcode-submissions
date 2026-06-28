class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1

        max_freq = max(dic.values())
        buckets = [[] for _ in range(max_freq + 1)]

        for num in dic:
            freq = dic[num]
            buckets[freq].append(num)

        print(buckets)
        res = []
        for freq in range(max_freq,0,-1):
            for i in buckets[freq]:
                if k > 0:
                    res.append(i)
                    k -= 1
                else:
                    return res
        return res
