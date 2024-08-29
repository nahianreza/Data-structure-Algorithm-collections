class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums)+ 1)]
        hmap = {}
        res = []

        for i in nums:
            hmap[i] = 1 + hmap.get(i,0)

        for num, v in hmap.items():
            count[v].append(num)

        for i in range(len(count) - 1, 0, -1):
            for j in count[i]:
                res.append(j)
                if len(res) == k:
                    return res
 

        