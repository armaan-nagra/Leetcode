class SparseVector:
    def __init__(self, nums: List[int]):
        self.length = len(nums)
        self.sparse_nums = []

        for i, x in enumerate(nums):
            if x != 0:
                self.sparse_nums.append((i, x))
        print(self.sparse_nums)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = j = 0
        res = 0
        while i < len(self.sparse_nums) and j < len(vec.sparse_nums):
            if self.sparse_nums[i][0] == vec.sparse_nums[j][0]:
                res += self.sparse_nums[i][1] * vec.sparse_nums[j][1]
                j += 1
                i += 1
            elif self.sparse_nums[i][0] < vec.sparse_nums[j][0]:
                i += 1
            else:
                j += 1
        
        return res





# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.idx_to_val = defaultdict(int)
#         for i, x in enumerate(nums):
#             if x != 0:
#                 self.idx_to_val[i] = x

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: "SparseVector") -> int:
#         res = 0

#         for i, x in vec.idx_to_val.items():
#             if i in self.idx_to_val:
#                 res += self.idx_to_val[i] * x
#         return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)