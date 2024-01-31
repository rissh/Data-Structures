
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        played = set()
        loss = collections.Counter()

        for winner, loser in matches:

            played.add(winner)
            played.add(loser)

            loss[loser] += 1

        ans = [[],[]]
        for player in sorted(played):
            if loss[player] == 0:
                ans[0].append(player)

            if loss[player] == 1:
                ans[1].append(player)

        return ans



