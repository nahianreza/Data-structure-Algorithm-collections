class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [[-i[1], i[0]] for i in count.items()]
        print(maxHeap)

        heapq.heapify(maxHeap)

        q = deque()
        res = ""
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                val = heapq.heappop(maxHeap)
                val[0] = val[0] + 1
                if val[0] != 0:
                    q.append([val, time + 1])
                res += val[1]
            if q:
                if q[0][1] == time:
                    temp = q.popleft()[0]
                    heapq.heappush(maxHeap, temp)
                
        for i in range(1,len(res)):
            if res[i] == res[i-1]:
                return ""
        else:
            return res

                


        


