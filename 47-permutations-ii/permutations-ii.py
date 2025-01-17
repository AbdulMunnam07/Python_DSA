class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return

            seen = set()  # To avoid duplicate permutations at this level
            for i in range(start, len(nums)):
                if nums[i] in seen:
                    continue  # Skip duplicate elements
                seen.add(nums[i])  # Mark this element as used at this level

                nums[start], nums[i] = nums[i], nums[start]  # Swap

                backtrack(start + 1)

                nums[start], nums[i] = nums[i], nums[start]  # Backtrack

        nums.sort()  # Sort the array to handle duplicates easily
        result = []
        backtrack(0)
        return result
