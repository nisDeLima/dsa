class Solution_rmvd:
    def originalDigits_rmvd(self, s: str) -> str:
        numbers_str = [
            "zero",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine"
        ]

        numbers_code = []

        for str_num in numbers_str:
            code = [0] * 26
            for c in str_num:
                code[ord(c) - ord("a")] += 1
            numbers_code.append(code)
        
        str_code = [0] * 26 

        for c in s:
            str_code[ord(c) - ord("a")] += 1
        
        self.numbers = []
        def match(code, code_check):
            for i in range(26):
                if code[i] < code_check[i]:
                    return False
            return True
        
        def remove(code, code_check):
            for i in range(26):
                code[i] -= code_check[i]
            return code
                
        def rec(code, numbers):
            if sum(code) == 0:
                self.numbers = numbers
                return True

            for idx, number_code in enumerate(numbers_code):
                if match(code, number_code):
                    if rec(remove(code.copy(), number_code), numbers + [str(idx)]):
                        return True
        rec(str_code, [])
        
        return "".join(sorted(self.numbers))
            

class Solution:
    def originalDigits(self, s: str) -> str:
        # Count frequency of each character
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Store how many of each digit we found
        digits = [0] * 10
        
        # Extract digits with unique letters FIRST
        digits[0] = count[ord('z') - ord('a')]  # zero - only 'z'
        digits[2] = count[ord('w') - ord('a')]  # two - only 'w'
        digits[4] = count[ord('u') - ord('a')]  # four - only 'u'
        digits[6] = count[ord('x') - ord('a')]  # six - only 'x'
        digits[8] = count[ord('g') - ord('a')]  # eight - only 'g'
        
        # Now extract digits with letters that become unique AFTER removing the above
        digits[3] = count[ord('h') - ord('a')] - digits[8]  # three (h appears in eight)
        digits[5] = count[ord('f') - ord('a')] - digits[4]  # five (f appears in four)
        digits[7] = count[ord('s') - ord('a')] - digits[6]  # seven (s appears in six)
        
        # Finally, the stragglers
        digits[9] = count[ord('i') - ord('a')] - digits[5] - digits[6] - digits[8]  # nine (i in five, six, eight)
        digits[1] = count[ord('n') - ord('a')] - digits[7] - 2 * digits[9]  # one (n in seven, and TWICE in nine)
        
        result = []
        for digit in range(10):
            result.append(str(digit) * digits[digit])
        
        return "".join(result)
