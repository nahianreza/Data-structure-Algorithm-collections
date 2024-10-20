class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem, c, u = 0, 0, set(nums)
        for i in u:
            if nums.count(i) > c:
                elem = i
                c = nums.count(i)
        return elem