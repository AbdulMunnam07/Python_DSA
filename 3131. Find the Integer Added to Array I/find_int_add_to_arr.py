class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        arr1 = min(nums1)
        arr2 = min(nums2)
        x = arr2 - arr1
        return x