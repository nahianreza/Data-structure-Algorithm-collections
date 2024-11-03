class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCount = Counter(p)
        sCount = Counter(s[:len(p)])

        res = [0] if pCount == sCount else []

        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                del sCount[s[l]]
            l+= 1

            if sCount == pCount:
                res.append(l)

        return res
        