class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newSet = set()
        for i in nums:
            if i in newSet:
                return True
            newSet.add(i)
        
        return False
                