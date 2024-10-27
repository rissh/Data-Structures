

class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        
        m = len(stayScore)
        dp = [[-1] * n for _ in range(k + 1)]

        def calculate(day, curr):
            if day == k:
                return 0
            if dp[day][curr] != -1:
                return dp[day][curr]

            max_points = stayScore[day][curr] + calculate(day + 1, curr)
            if n > 1:
                max_points = max(max_points, max(
                    travelScore[curr][next_city] + calculate(day + 1, next_city) 
                    for next_city in range(n) if next_city != curr
                ))
            dp[day][curr] = max_points
            return max_points

        return max(calculate(0, start) for start in range(n))
        
