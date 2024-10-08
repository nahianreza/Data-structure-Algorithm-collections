class TimeMap:

    def __init__(self):
        self.outerMap = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.outerMap:
            self.outerMap[key] = []
        self.outerMap[key].append((value, timestamp)) 
            

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        innerList = self.outerMap.get(key, [])

        l = 0
        r = len(innerList) - 1
        while r >= l:
            mid = (l + r) // 2
            if innerList[mid][1] == timestamp:
                res = innerList[mid][0]
                return res          
            elif innerList[mid][1] < timestamp:
                res = innerList[mid][0]
                l = mid + 1
            else:
                r = mid - 1


        return res

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)