class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap1 = collections.defaultdict(int)
        hmap2 = collections.defaultdict(int)

        for i in s1:
            hmap1[i] += 1

        length = 0
        for i in hmap1.values():
            length += i

        l = 0
        r = length - 1

        while r < len(s2):
            hmap2.clear()
            for c in range(l, r + 1):
                hmap2[s2[c]] += 1
            if hmap1 == hmap2:
                return True
            l += 1
            r += 1
            print(l)
            print(r)
        
        return False


        
        
        
            


        