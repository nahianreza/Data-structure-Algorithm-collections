# Go thru the list to input them in set and find duplicates
# If duplicate found then remove from original list
# return k

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1


        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        
        return l 


            



        
        
        
                    
        
        
            
        
        
        
        