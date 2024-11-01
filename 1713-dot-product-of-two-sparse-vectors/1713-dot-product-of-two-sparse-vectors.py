class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sparseMap = collections.defaultdict(int)

        for i, val in enumerate(self.nums):
            if val != 0:
                self.sparseMap[i] = val

        

        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        print(self.sparseMap)
        for i, val in self.sparseMap.items():
            if i in vec.sparseMap:
                res += val * vec.sparseMap[i]
        
        return res


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)