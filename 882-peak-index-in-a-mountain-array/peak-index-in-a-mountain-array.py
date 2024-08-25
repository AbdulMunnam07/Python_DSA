class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # res = max(arr)

        # for i in range(len(arr)):
        #     if arr[i] == res:
        #         return i

        left, right = 0, len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid 
            else:
                left = mid + 1

        return left
            


        