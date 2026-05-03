class Solution:
    def myAtoi(self, s: str) -> int:
        list_s = list(s)
        i = 0

        while i < len(s) and list_s[i] ==  " ":
            i += 1
        
        sign = 1

        if i < len(s) and list_s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and list_s[i] == "+":
            i += 1

        while i < len(s) and list_s[i] ==  "0":
            i += 1
        res = []

        while i < len(s) and list_s[i].isdigit():
            res.append(list_s[i])
            i += 1
        

        if not res:
            return 0

        num = int("".join(res)) * sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
