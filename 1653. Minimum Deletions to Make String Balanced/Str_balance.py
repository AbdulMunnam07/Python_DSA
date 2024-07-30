class Solution:
    def minimumDeletions(self, s):
        bCount = 0
        minDeletion = 0

        for ch in s:
            if ch == "a":
                minDeletion = min(minDeletion + 1, bCount)
            else:
                bCount += 1
        return minDeletion