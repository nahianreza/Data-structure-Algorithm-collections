class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        res = [0,0]
        for key, val in hmap.items():
            if val > res[1]:
                res = [key, val]
        return res[0]
        