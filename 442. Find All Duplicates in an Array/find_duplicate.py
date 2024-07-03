class Solution:
    def findDuplicates(nums):
        arr = [0] * (len(nums) +  1)

        for x in nums:
            arr[x] += 1

        res = []
        for i in range(len(nums)):
            if arr[i] == 2:
                res.append(i)

        return res
    
# findDuplicates([4,3,2,7,8,2,3,1])