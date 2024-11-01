class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for c in s:
            if len(stack) >= 2 and c == stack[-1] and c == stack[-2]:
                continue

            else:
                stack.append(c)

        return "".join(stack)
        