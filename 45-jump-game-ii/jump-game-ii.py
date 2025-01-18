class Solution:
    def jump(self, nums: List[int]) -> int:
        far = near = jumps = 0

        while far < len(nums) - 1:
            furtherest = 0
            for i in range(near, far + 1):
                furtherest = max(furtherest, i + nums[i])

            near = far + 1
            far = furtherest
            jumps += 1

        return jumps