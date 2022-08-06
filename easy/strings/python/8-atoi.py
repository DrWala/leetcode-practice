from curses.ascii import isdigit


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        sign = "+"
        if s[0] == "-" or s[0] == "+":
            sign = s[0]
            s = s[1:]

        if len(s) == 0:
            return 0

        if not s[0].isdigit():
            return 0

        chars = []
        for c in s:
            if not c.isdigit():
                break
            chars.append(c)

        num = int("".join(d for d in chars))
        num = num * -1 if sign == "-" else num
        if -2**31 <= num <= 2**31-1:
            return num

        if num < -2**31:
            return -2**31

        if num > 2**31 - 1:
            return 2**31 - 1

        return 0


# print(Solution().myAtoi("42"))
# print(Solution().myAtoi("      -42"))
# print(Solution().myAtoi("4193 with words"))
# print(Solution().myAtoi("words with 123"))
print(Solution().myAtoi("+1"))
