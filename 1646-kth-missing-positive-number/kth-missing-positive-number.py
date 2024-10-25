class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = [False] * 2002
        for ele in nums:
            res[ele] = True
        
        for i in range(1, len(res)):
            if not res[i]:
                k -= 1
                if k == 0:
                    return i
        return -1