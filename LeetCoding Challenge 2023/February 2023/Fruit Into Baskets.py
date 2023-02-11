
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        count = collections.defaultdict(int)
        left = 0
        total = 0
        res = 0

        for r in range(n):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                f = fruits[left]
                count[f] -= 1
                total -= 1
                left += 1

                if not count[f]:
                    count.pop(f)

            res = max(res,total)
        return res 
        
