class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, prefix, suffix = [0] * len(nums), [0] * len(nums), [0] * len(nums)


        prefix[0] = nums[0]
        for p in range(1, len(nums)):
            prefix[p] = nums[p] * prefix[p-1]

        suffix[len(nums) -1] = nums[len(nums) -1]
        for s in range(len(nums) -2, -1 , -1):
            suffix[s] = nums[s] * suffix[s+1]

        print(prefix)

        print(suffix)

        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[1]
            elif i == len(nums) - 1:
                res[i] = prefix[len(nums) - 2]
            else:
                res[i] = suffix[i + 1] * prefix[i - 1]
        
        return res


        





        