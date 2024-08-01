class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left, right = 0, len(height) - 1
        MaxLeft, MaxRight = height[left], height[right]

        res = 0
        while left < right:
            if MaxRight > MaxLeft:
                left += 1
                MaxLeft = max(MaxLeft, height[left])
                res += MaxLeft - height[left]

            else:
                right -= 1
                MaxRight = max(MaxRight, height[right])
                res += MaxRight - height[right]

        return res
