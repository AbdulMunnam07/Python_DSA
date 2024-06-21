class Solution:
    def plusOne(digits):
        num = ""

        for i in digits:
            num += str(i)

        add = str(int(num) + 1)

        digit = []
        for i in range(len(add)):
            digit.append(int(add[i]))

        return digit



# Time Complexity : O(n)
# Sapce Complexity : O(n)
