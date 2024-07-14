class Solution:
    def countKDifference(nums, k):
        seen = {}
        counter = 0
        for num in nums:
            if num - k in seen:
                counter += seen[num - k]
            if num + k in seen:
                counter += seen[num + k]
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        return counter
        