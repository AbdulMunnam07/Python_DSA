class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_non_zero(x):
            return '0' not in str(x)

        for a in range(1, n):
            b = n - a
            if is_non_zero(a) and is_non_zero(b):
                return [a, b]

         
        


        