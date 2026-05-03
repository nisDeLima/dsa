class Solution:
    def oddEvenJumps_tle(self, arr: List[int]) -> int:
        L = len(arr)
        answers = [[False, False] for _ in range(L)]  # odd, even
        answers[-1] = [True, True]

        def check_odd(l_idx, r_idx, odd_match):
            # want smallest value >= arr[l], tie -> smallest index
            if arr[r_idx] < arr[l_idx]:
                return False
            if odd_match is None:
                return True
            return (
                arr[r_idx] < arr[odd_match] or
                (arr[r_idx] == arr[odd_match] and r_idx < odd_match)
            )

        def check_even(l_idx, r_idx, even_match):
            # want largest value <= arr[l], tie -> smallest index
            if arr[r_idx] > arr[l_idx]:
                return False
            if even_match is None:
                return True
            return (
                arr[r_idx] > arr[even_match] or
                (arr[r_idx] == arr[even_match] and r_idx < even_match)
            )

        for l in range(L - 2, -1, -1):
            odd_match = None
            even_match = None

            for r in range(l + 1, L):
                if check_odd(l, r, odd_match):
                    odd_match = r
                if check_even(l, r, even_match):
                    even_match = r

            if odd_match is not None:
                answers[l][0] = answers[odd_match][1]
            if even_match is not None:
                answers[l][1] = answers[even_match][0]

        return sum(odd for odd, _ in answers)


    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        def make_next(indices):
            nxt = [-1] * n
            stack = []

            for i in indices:
                while stack and stack[-1] < i:
                    nxt[stack.pop()] = i
                stack.append(i)

            return nxt

        inc = sorted(range(n), key=lambda i: (arr[i], i))
        dec = sorted(range(n), key=lambda i: (-arr[i], i))

        next_higher = make_next(inc)
        next_lower  = make_next(dec)

        odd = [False] * n
        even = [False] * n
        odd[-1] = True
        even[-1] = True

        for i in range(n - 2, -1, -1):
            j = next_higher[i]
            if j != -1:
                odd[i] = even[j]

            k = next_lower[i]
            if k != -1:
                even[i] = odd[k]

        return sum(odd)
