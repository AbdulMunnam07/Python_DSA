class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        j = 0 
        m = len(spaces)

        for i in range(len(s)):
            if j < m and i == spaces[j]:
                res += " "
                j += 1

            res += s[i]

        return res
        