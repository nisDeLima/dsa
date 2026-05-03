class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        COMB_SIZE = len(digits)
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        curr_comb = []

        def form_digits(i):
            if len(curr_comb) == COMB_SIZE:
                res.append("".join(curr_comb))
                return
            if i >= COMB_SIZE:
                return

            digit = digits[i]
            for char in digit_to_char[digit]:
                curr_comb.append(char)
                form_digits(i + 1)
                curr_comb.pop()
        form_digits(0)
        return res
