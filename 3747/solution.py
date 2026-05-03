class Solution(object):
    def countDistinct(self, n):
        s = str(n)
        m = len(s)

        # pow9[i] = 9^i
        pow9 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow9[i] = pow9[i - 1] * 9

        # 1) count all zero-free numbers with fewer digits than n
        ans = 0
        for length in range(1, m):
            ans += pow9[length]

        # 2) count zero-free numbers of the same length <= n
        i = 0
        while i < m:
            if s[i] == '0':
                break

            digit = ord(s[i]) - ord('0')

            # digits 1..(digit-1) allowed here
            ans += (digit - 1) * pow9[m - i - 1]

            i += 1

        # 3) if we matched all digits, n itself is zero-free
        return ans + (1 if i == m else 0)

