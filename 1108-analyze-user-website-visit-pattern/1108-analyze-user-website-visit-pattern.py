from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        patternList = collections.defaultdict(list)

        for time, key, val in sorted(zip(timestamp,username, website)):
            patternList[key].append(val)
        
        count = collections.defaultdict(int)

        for key, val in patternList.items():
            for combo in set(combinations(val, 3)):
                count[combo] += 1
        
        maxPattern = ""
        maxVal = 0

        for key,val in count.items():
            if val > maxVal or (val == maxVal and key < maxPattern):
                maxVal = val
                maxPattern = key
        
        return maxPattern






        


        
        