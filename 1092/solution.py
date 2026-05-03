class Solution:
    # --- Version 1: BFS brute-force exploration ---
    # This version tries every possible interleaving of str1 and str2
    # to find the shortest sequence containing both as subsequences.
    # It's conceptually valid, but painfully inefficient — BFS explores
    # a combinatorial explosion of states, many of which are redundant.
    # Good for learning, bad for performance.
    def shortestCommonSupersequence_bfs(self, str1: str, str2: str) -> str:
        queue = deque([(0, 0, "")])  # (index in str1, index in str2, current supersequence)
        visited = set([(0, 0, "")])  # prevents revisiting identical states

        while queue:
            i, j, seq = queue.popleft()

            # Base case: both strings are fully processed
            if i == len(str1) and j == len(str2):
                return seq

            # Case 1: matching chars → advance both
            if i < len(str1) and j < len(str2) and str1[i] == str2[j]:
                nxt = (i + 1, j + 1, seq + str1[i])
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
            else:
                # Case 2: mismatch → try advancing each side separately
                if i < len(str1):
                    nxt = (i + 1, j, seq + str1[i])
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
                if j < len(str2):
                    nxt = (i, j + 1, seq + str2[j])
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

    # --- Version 2: LCS-guided efficient approach ---
    # The logic here is smarter:
    #   1. Find the Longest Common Subsequence (LCS) — the shared backbone
    #      that must appear in order in both strings.
    #   2. Build the Shortest Common Supersequence (SCS) by weaving in
    #      the non-LCS characters around that backbone.
    #
    # This works because any optimal SCS must preserve the LCS order,
    # and every character not in the LCS must be inserted around it.
    #
    # Example:
    #   str1 = "abac", str2 = "cab"
    #   LCS = "ab"
    #   Result SCS = "cabac"
    #
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Step 1. Compute LCS using memoized recursion
        @cache
        def get_lcs(i: int, j: int) -> str:
            # End of one string → no common subsequence
            if i == len(str1) or j == len(str2):
                return ""
            # Matching characters contribute to LCS
            if str1[i] == str2[j]:
                return str1[i] + get_lcs(i + 1, j + 1)
            # Otherwise, explore both skips and choose the longer result
            l1 = get_lcs(i + 1, j)
            l2 = get_lcs(i, j + 1)
            return l1 if len(l1) >= len(l2) else l2

        lcs = get_lcs(0, 0)
        scs = []
        p1 = p2 = p_lcs = 0

        # Step 2. Merge both strings guided by the LCS
        while p1 < len(str1) and p2 < len(str2) and p_lcs < len(lcs):
            char1, char2, common = str1[p1], str2[p2], lcs[p_lcs]

            # If both chars match the LCS, we include it once
            if char1 == common == char2:
                scs.append(common)
                p1 += 1
                p2 += 1
                p_lcs += 1
            # Otherwise, include non-LCS chars from either side
            if char1 != common:
                scs.append(char1)
                p1 += 1
            if char2 != common:
                scs.append(char2)
                p2 += 1

        # Step 3. Append leftovers from both strings
        scs.extend(str1[p1:])
        scs.extend(str2[p2:])

        return "".join(scs)
