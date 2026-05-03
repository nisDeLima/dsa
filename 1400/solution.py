class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        counter = Counter(s)
        num_even_pairs = 0
        num_odds = 0

        for key, count in counter.items():
            evens = count // 2
            odds = count % 2
            num_even_pairs += evens
            num_odds += odds

        if num_odds > k:
            return False

        return True
