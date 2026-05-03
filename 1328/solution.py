class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        odd_len = len(palindrome) % 2 != 0
        odd_mid = None

        if odd_len:
            odd_mid = len(palindrome) // 2
        
        switched = False
        for i in range(len(palindrome)):
            if odd_len and i == odd_mid:
                continue
            if palindrome[i] != "a":
                palindrome = palindrome[:i] + "a" + palindrome[i + 1:]
                switched = True
                break
        
        if not switched:
            palindrome = palindrome[:-1] + "b"
        
        return palindrome
