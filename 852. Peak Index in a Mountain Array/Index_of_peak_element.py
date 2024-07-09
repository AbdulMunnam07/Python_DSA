class Solution:
    def peakIndexInMountainArray(arr):
        res = max(arr)

        for i in range(len(arr)):
            if arr[i] == res:
                return i
            


        