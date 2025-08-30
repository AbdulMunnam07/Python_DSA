class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n   # <-- why n, not m?
        for i in range(1, m):
            for j in range(1, n):
                left = rows[j - 1]
                up = rows[j]
                rows[j] = left + up
        return rows[-1]
