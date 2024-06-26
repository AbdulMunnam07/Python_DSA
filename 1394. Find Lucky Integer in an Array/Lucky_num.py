class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = [-1]

        Set = set(arr)

        for i in Set:
            if arr.count(i) == i:
                ans.append(i)
        output = max(ans)
        return output
        