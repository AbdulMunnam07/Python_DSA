class Solution:
    def sortArrayByParity(nums):
        # arr = []
        # for i in range(len(nums)):
        #     if nums[i] % 2 == 0:
        #         arr.append(nums[i])

        #     elif nums[i] == 0:
        #         arr.append(nums[i])

        # for i in range(len(nums)):
        #     if nums[i] % 2 != 0:
        #         arr.append(nums[i])

        # return arr


        # Here is the alternative Solution

        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                arr1.append(nums[i])

            elif nums[i] % 2 != 0:
                arr2.append(nums[i])

        return arr1 + arr2