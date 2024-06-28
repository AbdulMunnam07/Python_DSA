class Solution:
    def merge(nums1, m, nums2, n):
        n = len(nums1) - m

        for i in range(n):
            nums1.pop()

        nums1.extend(nums2)
        nums1.sort()
        return nums1