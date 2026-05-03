class Solution:
    def decodeString_rmvd(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                word = []
                while stack and not stack[-1].isdigit():
                    curr = stack.pop()
                    if curr != "[":
                        word.append(curr)
                multiplier = []
                while stack and stack[-1].isdigit():
                    multiplier.append(stack.pop())
                mult_int = int("".join(reversed(multiplier))) if multiplier else 1
                new_str = "".join(reversed(word)) * mult_int
                stack.append(new_str)
                continue
            stack.append(char)

        return "".join(stack) 

    def decodeString(self, s: str) -> str:
        str_stack = []
        num_stack = []

        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                str_stack.append(curr)
                num_stack.append(num)
                curr = ""
                num = 0
            elif ch == "]":
                prev = str_stack.pop()
                mult = num_stack.pop()
                curr = prev + curr * mult
            else:
                curr += ch

        return curr 
