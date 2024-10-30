class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hmap = {key:val for val,key in enumerate(nums1)}

        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                newVal = stack.pop()
                res[hmap[newVal]] = nums2[i]

            if nums2[i] in hmap:
                stack.append(nums2[i])
        
        return res
            
            
                



        
                
        
        return res
        