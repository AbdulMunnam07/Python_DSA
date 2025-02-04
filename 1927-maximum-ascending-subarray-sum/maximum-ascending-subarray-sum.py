class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        currentSubarraySum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                maxSum = max(maxSum, currentSubarraySum)
                currentSubarraySum = 0
            currentSubarraySum += nums[i]
        return max(maxSum, currentSubarraySum)