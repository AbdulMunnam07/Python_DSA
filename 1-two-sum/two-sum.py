class Solution:
    def twoSum(self, nums, target):
        numMap = {}
        n = len(nums)

        for i in range(n):
            res_val = target - nums[i]
            if res_val in numMap:
                return [numMap[res_val], i]
            numMap[nums[i]] = i
        
        return []