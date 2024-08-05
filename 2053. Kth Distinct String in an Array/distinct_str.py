class Solution:
    def kthDistinct(self, arr, k):
        distinction = set()
        seen = set()

        for s in arr:
            if s in seen:
                distinction.discard(s)
            else:
                distinction.add(s)
                seen.add(s)

        for s in arr:
            if s in distinction:
                k -= 1
                if k == 0:
                    return s

        return ""