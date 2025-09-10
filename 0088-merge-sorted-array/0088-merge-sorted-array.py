class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # i, j, k = m - 1, n - 1, m + n - 1

        # while j>=0:
        #     if i>=0 and nums1[i] > nums2[j]:
        #         nums1[k] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[k] = nums2[j]
        #         j -= 1
        #     k -= 1

        a = nums1[:m]
        b = nums2[:n]

        i = j = 0
        merged = []

        while i < m and j < n:
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])

        nums1[:m+n] = merged