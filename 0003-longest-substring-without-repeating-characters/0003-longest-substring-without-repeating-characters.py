class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        newSet = set()
        count = 0

        while r < len(s):
            while s[r] in newSet:
                newSet.remove(s[l])
                l += 1
            newSet.add(s[r])
            count = max(count, r - l + 1)
            r += 1
           

        return count    
        