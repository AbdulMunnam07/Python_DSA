class Solution(object):
    def findDifference(nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        c = s1 & s2
        
        return [s1-c, s2-c]