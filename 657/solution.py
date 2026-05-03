class Solution:
    def judgeCircle(self, moves: str) -> bool:
        counter = Counter(moves)
        return counter["R"] == counter["L"] and counter["U"] == counter["D"]
