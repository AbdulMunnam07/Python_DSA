class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        res = max(arr)

        for i in range(len(arr)):
            if arr[i] == res:
                return i
            


        