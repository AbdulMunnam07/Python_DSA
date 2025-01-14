class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_arr = n * [0]

        for curr_indx in range(n):
            common_count = 0
            for a_index in range(curr_indx + 1):
                for b_index in range(curr_indx + 1):
                    if A[a_index] == B[b_index]:
                        common_count += 1
                        break
            prefix_common_arr[curr_indx] = common_count
        return prefix_common_arr