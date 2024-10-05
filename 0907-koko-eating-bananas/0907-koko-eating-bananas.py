# Total = 27
#
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        k = r

        while r >= l:
            mid = (l + r) // 2
            total = 0
            for i in piles:
                total += math.ceil(i / mid)

            if total <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return k
        