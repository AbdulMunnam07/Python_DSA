class Solution:
    def createTargetArray(self, nums, index):
        target = []

        for (num, idx) in zip(nums, index):
            target.insert(idx, num)

        return target
        