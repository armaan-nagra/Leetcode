class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merge the two arrays and then find median? have two counters?
        temp = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            temp.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            temp.append(nums2[j])
            j += 1
        
        n = len(temp)

        mid = n // 2
        if n % 2 == 1:
            return float(temp[mid])
        else:
            return (temp[mid - 1] + temp[mid]) / 2.0