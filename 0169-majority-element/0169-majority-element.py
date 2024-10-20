class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem, maj_cnt = 0, 0
        u = set(nums)
        med = len(nums) // 2
        for i in u:
            c = nums.count(i)
            if c > med:
                return i
            elif c > maj_cnt:
                elem = i
                maj_cnt = nums.count(i)
        return elem