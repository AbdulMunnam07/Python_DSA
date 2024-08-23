class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in nums:
        #     count = 0
        #     for num in nums:
        #         if num < i:
        #             count += 1
        #     res.append(count)
        # return res
        num = sorted(nums)
        dictionary = {}
        for i in range(len(num)):
            if num[i] not in dictionary:
                dictionary[num[i]] = i

        ans = []
        for j in range(len(nums)):
            ans.append(dictionary[nums[j]])

        return ans

