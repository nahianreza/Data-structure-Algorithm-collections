class DetectSquares:

    def __init__(self):
        self.countMap = collections.defaultdict(int)
        self.countList = []
        

    def add(self, point: List[int]) -> None:
        self.countMap[tuple(point)] += 1
        self.countList.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        dx, dy = point
        for x, y in self.countList:
            if (abs(dx-x) != abs(dy-y)) or dx == x or dy == y:
                continue
            res += self.countMap[(x, dy)] * self.countMap[(dx, y)]
        
        return res

            

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)