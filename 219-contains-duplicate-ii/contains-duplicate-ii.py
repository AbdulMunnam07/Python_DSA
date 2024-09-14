class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = {}
        for i in range(len(nums)):
            if nums[i] in hashSet and i - hashSet[nums[i]] <= k:
                return True
            hashSet[nums[i]] = i
        return False