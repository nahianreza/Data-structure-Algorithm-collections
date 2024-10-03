class Solution:
    def maxArea(self, height: List[int]) -> int:
        mArea = 0
        l = 0
        r = len(height) - 1

        while r > l:
            curHeight = min(height[r], height[l])
            width = r - l
            total = curHeight * width
            mArea = max(mArea, total)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return mArea
        