class Solution(object):
    def intersection(self, nums1, nums2):
        # Set = set()

        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             Set.add(j)

        # return Set

        res = []

        for value in nums1:
            if value not in res and value in nums2:
                res.append(value)

        return res
        