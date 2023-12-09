class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        for winner, loser in matches:
            loss_count[loser] = loss_count.get(loser, 0) + 1
            loss_count[winner] = loss_count.get(winner, 0)


        zero_loss = [player for player, losses in loss_count.items() if losses == 0]
        one_loss = [player for player, losses in loss_count.items() if losses == 1]


        zero_loss.sort()
        one_loss.sort()

        return [zero_loss, one_loss]