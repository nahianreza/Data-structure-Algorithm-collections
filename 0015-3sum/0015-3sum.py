class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resList = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1

            while r > l:
                total = nums[r] + nums[l] + nums[i]
                if total == 0:
                    resList.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                    
                elif total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
        
        return resList
                    



        
        



        