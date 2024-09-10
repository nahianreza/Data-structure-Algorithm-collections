class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []

        for i in points:
            eDist = ((0 - i[0])**2 + (0 - i[1])**2)** 1/2
            
            heapq.heappush(heap, (eDist, [i[0], i[1]]))
        
        for i in range(k):
            key, value = heapq.heappop(heap)
            res.append(value)
        
        return res
        
        