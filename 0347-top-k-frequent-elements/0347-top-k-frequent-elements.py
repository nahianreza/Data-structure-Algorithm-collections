class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        hmap = {}
        res = []

        for i in nums:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 0

        hmap = dict(sorted(hmap.items(), key= lambda item: item[1], reverse = True))

        return list(hmap.keys())[:k]
        

        