class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # arr = []

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         arr.append(i)

        # if not arr:
        #     return [-1, -1]            
        # return (arr[0], arr[-1])

        def binary_search(nums, target, is_searching_left):
            l, r = 0, len(nums) - 1
            idx = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        r = mid - 1
                    else:
                        l = mid + 1
            return idx

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)

        return [left, right]