class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if len(votes) == 1:
            return votes[0]

        counts = {team: [0] * len(votes[0]) for team in votes[0]}

        for vote in votes:
            for position, team in enumerate(vote):
                counts[team][position] += 1
        return ''.join(sorted(counts, key=lambda t: ([-c for c in counts[t]], t)))
