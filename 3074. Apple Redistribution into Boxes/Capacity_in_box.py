class Solution:
    def minimumBoxes(self, apple, capacity):
        ans = 0
        sum_apple = sum(apple)
        capacity.sort()

        i = len(capacity) - 1
        while i >= 0:
            sum_apple -= capacity[i]
            ans += 1
            if sum_apple <= 0:
                break
            i -= 1

        return ans


        