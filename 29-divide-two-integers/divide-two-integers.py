class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # I do this for my happiness I've solve question in one attempt
        # result = dividend/divisor
        # return int(result)

        int_max = 2**31 - 1
        int_min = -2**31

        if dividend == int_min and divisor == -1:
            return int_max
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            quotient += multiple
            dividend -= temp

        return sign * quotient
        
