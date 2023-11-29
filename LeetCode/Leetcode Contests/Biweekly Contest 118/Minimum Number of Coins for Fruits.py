
def f(currInd, totalItem, prices, remainOffer, dp):
    if currInd == totalItem:
        return 0
    if currInd > totalItem:
        return float('inf')

    if dp[currInd][remainOffer] != -1:
        return dp[currInd][remainOffer]

    if remainOffer:
        dp[currInd][remainOffer] = min(
            prices[currInd] + f(currInd + 1, totalItem, prices, currInd + 1, dp),
            f(currInd + 1, totalItem, prices, remainOffer - 1, dp)
        )
        return dp[currInd][remainOffer]

    dp[currInd][remainOffer] = prices[currInd] + f(currInd + 1, totalItem, prices, currInd + 1, dp)
    return dp[currInd][remainOffer]

class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        return f(0, n, prices, 0, dp)
    