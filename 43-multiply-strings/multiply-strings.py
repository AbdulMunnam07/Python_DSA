class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_as_integer = int(num1)
        num2_as_integer = int(num2)

        result = (num1_as_integer * num2_as_integer)
        return str(result)