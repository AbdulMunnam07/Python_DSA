class Solution:
    def sortArrayByParity(self ,nums):
        a1 = []
        a2 = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                a1.append(nums[i])
            else:
                a2.append(nums[i])
        return a1 + a2







   






















        # left, right = 0, len(nums) - 1
        # ans = [0]*len(nums)
        # for i in nums:
        #     if i % 2 == 0:
        #         ans[left] = i
        #         left += 1
        #     else:
        #         ans[right] = i
        #         right -= 1

        # return ans

        