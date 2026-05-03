from collections import Counter

class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        n = len(s)
        
        # Track first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
        
        for idx, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = idx
            last_occurrence[char] = idx
        
        char_count = Counter(s)
        valid_intervals = []
        
        # Try all possible ranges [i, j]
        for start_char, i in first_occurrence.items():
            for end_char, j in last_occurrence.items():
                if i > j:
                    continue
                
                # Check if [i, j] is a valid special substring
                # Count how many character occurrences are fully contained in [i, j]
                contained_char_count = 0
                
                for char in char_count:
                    # Is this character fully contained in range [i, j]?
                    if first_occurrence[char] >= i and last_occurrence[char] <= j:
                        contained_char_count += char_count[char]
                
                # Valid if: all chars in range are accounted for AND not entire string
                substring_length = j - i + 1
                if contained_char_count == substring_length and substring_length < n:
                    valid_intervals.append((i, j))
        
        # Remove duplicate intervals
        valid_intervals = list(set(valid_intervals))
        
        # Sort by length (greedy: prefer shorter intervals for better packing)
        valid_intervals.sort(key=lambda x: x[1] - x[0])
        
        # Greedily select non-overlapping intervals
        selected = []
        
        for start, end in valid_intervals:
            # Check if this interval overlaps with any already selected
            if all(end < sel_start or start > sel_end for sel_start, sel_end in selected):
                selected.append((start, end))
                
                if len(selected) >= k:
                    return True
        
        return len(selected) >= k
