class Solution:
    def reorganizeString(self, s: str) -> str:
        countMap = Counter(s)

        maxHeap = [[-i[1],i[0]] for i in countMap.items()]


        q = deque()

        res = ""
        time = 0

        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap: 
                val, c = heapq.heappop(maxHeap)
                val += 1
                res += c
                if val != 0:
                    q.append([[val, c], time + 1])
            if q and q[0][1] == time:
                new_heap = q.popleft()[0]
                heapq.heappush(maxHeap, new_heap)

        print(res)

        for i in range(1,len(res)):
            if res[i-1] == res[i]:
                return ""
        else:
            return res


