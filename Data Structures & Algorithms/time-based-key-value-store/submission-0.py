class TimeMap:

    def __init__(self):
        self.map = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        value = self.map.get(key, [])
        low, high = 0, len(value) - 1
        res = ''
        while low <= high:
            mid = (low+high)//2
            if value[mid][1] <= timestamp:
                res = value[mid][0]
                low = mid + 1
            else:
                high = mid - 1
        return res
