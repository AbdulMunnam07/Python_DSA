class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def countTrees(m):
            if m <= 1:
                return 1
            if m in memo:
                return memo[m]

            total = 0
            for root in range(1, m + 1):
                left = countTrees(root - 1)
                right = countTrees(m - root)
                total += left * right

            memo[m] = total
            return total

        return countTrees(n)
