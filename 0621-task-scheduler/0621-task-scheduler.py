class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        numIntervals = 0


        q = collections.deque()

        freqMap = Counter(tasks)

        maxHeap = [-1 * i[1] for i in freqMap.items()]
        print(maxHeap)

        heapq.heapify(maxHeap)

        while maxHeap or q:
            numIntervals += 1

            if maxHeap:
                val = 1 + heapq.heappop(maxHeap)
                if val != 0:
                    q.append((val, n + numIntervals))
            
            if q and q[0][1] == numIntervals:
                count = q.popleft()
                heapq.heappush(maxHeap, count[0])

        return numIntervals






        



        
        