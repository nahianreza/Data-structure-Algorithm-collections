# Use a count hashmap to get the count of unique characters
# Fill the list with number of unique characters

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        def swap(x, y):
            temp = nums[x]
            nums[x] = nums[y]
            nums[y] = temp
        
        i = 0
        l, r = 0 , len(nums) - 1

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
            elif nums[i] == 2:
                swap(r, i)
                r -= 1
                i -= 1
            i += 1
            
            
        
        
        
        