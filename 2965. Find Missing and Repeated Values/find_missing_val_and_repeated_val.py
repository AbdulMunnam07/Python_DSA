class Solution:
    def findMissingAndRepeatedValues(grid):
        arr = []
        for i in grid:
            for j in i:
                arr.append(j)
        
        ans = []
        for i in arr:
            if arr.count(i) > 1 :
                ans.append(i)
                break


        n = len(grid)**2
        for i in range(1, n + 1):
            if i not in arr:
                ans.append(i)

        return ans

        