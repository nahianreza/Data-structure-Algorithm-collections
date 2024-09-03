class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while right > left:
            res = numbers[right] + numbers[left]
            if res == target:
                return [left + 1, right + 1]
            elif res < target:
                left += 1
            else:
                right -= 1
        
        