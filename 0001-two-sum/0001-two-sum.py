class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}


        for i in range(len(nums)):
            res = target - nums[i]
            if res in hmap:
                return [i, hmap[res]]
            hmap[nums[i]] = i
                
        
