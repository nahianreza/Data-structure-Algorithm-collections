class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while r >= l:
            mid = (r + l) // 2
            cur = nums[mid]
            if cur == target:
                return mid
            if cur >= nums[l]:
                if target > cur or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < cur or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1


        