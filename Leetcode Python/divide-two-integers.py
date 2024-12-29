class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """ Brute force
        if dividend == 0:
            return 0
        if divisor == 0:
            return False
        if dividend < 0 and divisor < 0:
            mult = 1
        elif dividend < 0 or divisor < 0:
            mult = -1
        else:
            mult = 1
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        dec = 0
        while dividend != 0:
            print(dividend, divisor)
            if dec > 4:
                break
            if dividend >= divisor:
                if dec > 0:
                    dec +=1
                    ans += 0.1
                    dividend -= divisor
                else:
                    ans += 1
                    dividend -= divisor
            else:
                dec += 1
                dividend = dividend*(dec*10) - divisor
                ans += 0.1
        return int(ans*mult)
        """
        # Bit shift
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        negative = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            current_divisor, num_divisors = divisor, 1

            while dividend >= (current_divisor << 1):
                current_divisor <<= 1
                num_divisors <<= 1

            dividend -= current_divisor
            quotient += num_divisors

        if negative:
            quotient = -quotient

        return max(min(quotient, 2**31 - 1), -2**31)
if __name__ == "__main__":
    solution  = Solution()
    dividend = 7
    divisor = -3
    result = solution.divide(dividend, divisor)
    print(result)
