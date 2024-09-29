import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        i, j = 0, 0
        
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1

     
        while i < len(nums1):
            arr.append(nums1[i])
            i += 1

      
        while j < len(nums2):
            arr.append(nums2[j])
            j += 1

  
        n = len(arr)
        if n % 2 == 1:
            median = arr[n // 2]
        else:
            median = (arr[n // 2 - 1] + arr[n // 2]) / 2.0

        return median