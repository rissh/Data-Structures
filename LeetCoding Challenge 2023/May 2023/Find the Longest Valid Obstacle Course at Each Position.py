
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        n = len(obstacles)
        ans = []
        dp = [10**8] * (n+1)

        for ob in obstacles:
            ind = bisect.bisect(dp,ob)
            ans.append(ind + 1)
            dp[ind] = ob

        return ans
        
