class Solution:
    def arraySign(nums):
        prod = 1
        for i in nums:
            prod *= i

        if prod > 0:
            return 1

        elif prod < 0:
            return -1

        else:
            return 0
        