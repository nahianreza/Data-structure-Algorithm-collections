class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        count = 0
        maxRooms = 0

        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])

        s, e = 0, 0

        while s < len(start):
            if start[s] != end[e] and min(start[s], end[e]) == start[s]:
                count += 1
                s+= 1
            else:
                count -= 1
                e += 1
            maxRooms = max(maxRooms, count)
        
        return maxRooms
            
        
        