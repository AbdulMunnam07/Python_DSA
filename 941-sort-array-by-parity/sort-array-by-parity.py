class Solution:
    def sortArrayByParity(self ,nums):
        # arr1 = []
        # arr2 = []

        # for i in range(len(nums)): 
        #     if nums[i] % 2 == 0:
        #         arr1.append(nums[i])

        #     elif nums[i] % 2 != 0:
        #         arr2.append(nums[i])

        # return arr1 + arr2


        left, right = 0, len(nums) - 1
        ans = [0]*len(nums)
        for i in nums:
            if i % 2 == 0:
                ans[left] = i
                left += 1
            else:
                ans[right] = i
                right -= 1

        return ans

        