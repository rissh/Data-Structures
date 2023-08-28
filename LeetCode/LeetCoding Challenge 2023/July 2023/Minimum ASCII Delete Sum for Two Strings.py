
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return self.solve(s1, s2, 0, 0, dp)

    def solve(self, s1: str, s2: str, i: int, j: int, dp: list[list[int]]) -> int:
        if dp[i][j] != -1:
            return dp[i][j]
        if i == len(s1):
            return sum(ord(ch) for ch in s2[j:])
        if j == len(s2):
            return sum(ord(ch) for ch in s1[i:])
        nt = min(ord(s1[i]) + self.solve(s1, s2, i + 1, j, dp), ord(s2[j]) + self.solve(s1, s2, i, j + 1, dp))
        tk = float('inf')
        if s1[i] == s2[j]:
            tk = self.solve(s1, s2, i + 1, j + 1, dp)
        dp[i][j] = min(nt, tk)
        return dp[i][j]
