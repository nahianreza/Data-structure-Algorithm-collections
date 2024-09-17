class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

    
        if len(s) == 1:
            return 1


        res = 0
        l = 0
        r = 0

        hmap = collections.defaultdict(int)
        while r < len(s):
            curr = s[r]
            hmap[curr] += 1
            while (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res
            
            

        






