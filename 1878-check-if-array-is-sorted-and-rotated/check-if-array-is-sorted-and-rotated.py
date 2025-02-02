class Solution:
    def check(self, nums: List[int]) -> bool:
        sizeOfArray = len(nums)

        sorted_array = sorted(nums)

        for i in range(sizeOfArray):
            is_matched = True
            for index in range(sizeOfArray):
                if nums[(i + index) % sizeOfArray] != sorted_array[index]:
                    is_matched = False
                    break
                
            if is_matched:
                return True

        return False