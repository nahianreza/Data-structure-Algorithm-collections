class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = collections.Counter(tasks)

        mHeap = [-s for s in count.values()]
        heapq.heapify(mHeap)

        q = collections.deque()
        time = 0
        while mHeap or q:
            time += 1

            if mHeap:
                val = 1 + heapq.heappop(mHeap)
                if val:
                    q.append((val, time + n))
            
            if q and q[0][1] == time:
                heapq.heappush(mHeap, q.popleft()[0])
        
        return time




        
        