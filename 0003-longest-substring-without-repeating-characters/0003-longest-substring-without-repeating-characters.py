class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        res = 0 

        l = 0

        for r in range(1,len(s)):
            while s[r] in s[l: r]:
                l += 1
            res = max(res, r - l + 1)

        return res

            