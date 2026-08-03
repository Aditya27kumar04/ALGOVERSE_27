class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 1. Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # If string contains only spaces
        if i == n:
            return 0

        # 2. Check sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # 3. Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Overflow check
            if num > (2**31 - 1 - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1

            num = num * 10 + digit
            i += 1

        return sign * num