class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If the strings are already equal, no swap is needed.
        if s1 == s2:
            return True
        # Find the indices where s1 and s2 differ.
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
            # Early exit if more than 2 differences are found.
            if len(diff) > 2:
                return False

        # We must have exactly 2 differences for a single swap to fix them.
        if len(diff) != 2:
            return False

        i, j = diff
        # Check if swapping s1[i] and s1[j] would make s1 equal to s2.
        return s1[i] == s2[j] and s1[j] == s2[i]