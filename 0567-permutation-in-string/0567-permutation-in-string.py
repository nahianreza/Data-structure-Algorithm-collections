class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hmap1 = collections.defaultdict(int)
        hmap2 = collections.defaultdict(int)

        for i in s1:
            hmap1[i] += 1
        
        for j in range(len(s1)):
            hmap2[s2[j]] += 1



        if hmap1 == hmap2:
            return True
        

        for i in range(len(s1), len(s2)):
            prev = s2[i - len(s1)]
            hmap2[prev] -= 1

            if hmap2[prev] == 0:
                del hmap2[prev]
            
            cur = s2[i]
            hmap2[cur] += 1

            if hmap2 == hmap1:
                return True
        
        return False
