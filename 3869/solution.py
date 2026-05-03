class Solution:
    def countFancy(self, l: int, r: int) -> int:
        def is_good(n):
            digits = [int(d) for d in str(n)]
            if len(digits) <= 1:
                return True
            inc = all(digits[i] < digits[i + 1] for i in range(len(digits) - 1))
            dec = all(digits[i] > digits[i + 1] for i in range(len(digits) - 1))
            return inc or dec

        good_sums = set(s for s in range(0, 200) if is_good(s))

        def count_fancy_up_to(num):
            digits = str(num)
            n = len(digits)

            @cache
            def dp(pos, tight, prev_digit, still_increasing, still_decreasing, started, digit_sum):
                if pos == n:
                    if not started:
                        return 0
                    number_is_good = still_increasing or still_decreasing
                    digit_sum_is_good = digit_sum in good_sums
                    return 1 if (number_is_good or digit_sum_is_good) else 0

                max_digit = int(digits[pos]) if tight else 9
                total = 0

                for d in range(0, max_digit + 1):
                    new_tight = tight and (d == max_digit)
                    if not started and d == 0:
                        total += dp(pos + 1, new_tight, -1, True, True, False, 0)
                    else:
                        new_inc = still_increasing and (prev_digit == -1 or d > prev_digit)
                        new_dec = still_decreasing and (prev_digit == -1 or d < prev_digit)
                        total += dp(pos + 1, new_tight, d, new_inc, new_dec, True, digit_sum + d)

                return total

            result = dp(0, True, -1, True, True, False, 0)
            dp.cache_clear()
            return result

        return count_fancy_up_to(r) - count_fancy_up_to(l - 1)
