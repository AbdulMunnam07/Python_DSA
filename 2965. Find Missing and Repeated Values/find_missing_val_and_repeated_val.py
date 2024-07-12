class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)
        
        ans = []
        for i in arr:
            if arr.count(i) > 1 :
                ans.append(i)
                break

        print(ans)

        n = len(grid)**2
        for i in range(1, n + 1):
            if i not in arr:
                ans.append(i)

        return ans

        