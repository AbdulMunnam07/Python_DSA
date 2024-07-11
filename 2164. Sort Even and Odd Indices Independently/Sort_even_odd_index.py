class Solution:
    def sortEvenOdd(nums):
        odd,even = [],[]
        for i in range(len(nums)):
            if i % 2 ==0:
                even.append(nums[i])

            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        print(odd,even)
        res = []
        for i in range(len(even)):
            res.append(even[i])
            if len(odd) > i:
                res.append(odd[i])
        print(res)
        return res