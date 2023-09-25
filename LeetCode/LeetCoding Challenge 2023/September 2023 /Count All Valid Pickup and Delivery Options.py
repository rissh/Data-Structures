
class Solution:
    def countOrders(self, n: int) -> int:

        # 2 * n -> Total Slots
        # Count valid ways to array a pair P1, D1 and so on
        # x * (x - 1) -> Total Choices
        # x * (x - 1) // 2-> Valid Choices

        slots = 2 * n
        res = 1

        while slots:
            valid = slots * (slots - 1) // 2
            res *= valid
            slots -= 2

        return res % (10 ** 9 + 7)
      
