class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cur = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    cur += 1

        return cur
                
        