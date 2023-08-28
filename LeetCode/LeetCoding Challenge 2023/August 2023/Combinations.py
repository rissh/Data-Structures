
lass Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []

        def back(start, comb):
            if len(comb) == k:
                ans.append(comb.copy())
                return 

            for i in range(start, n + 1):
                comb.append(i)
                back(i + 1, comb)
                comb.pop()

        back(1, [])
        return ans
