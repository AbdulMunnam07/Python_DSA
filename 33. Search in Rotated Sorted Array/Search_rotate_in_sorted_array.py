class Solution:
    def search(nums: List[int], target: int):
        for i in range(len(nums)):
            if nums[i] == target: 
                return i

        return -1