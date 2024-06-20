class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            count = 0
            for num in nums:
                if num < i:
                    count += 1
            res.append(count)
        return res
