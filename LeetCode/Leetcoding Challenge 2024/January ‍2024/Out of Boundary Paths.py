
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        row = m
        col = n
        mod = 10**9+7
        dp = [[0] * col for r in range(row)]

        for m in range(1, maxMove + 1):
            tmp = [[0] * col for r in range(row)]
            for r in range(row):
                for c in range(col):
                    if r + 1 == row:
                        tmp[r][c] = (tmp[r][c] + 1) % mod
                    else:
                        tmp[r][c] = (tmp[r][c] + dp[r + 1][c]) % mod

                    if r - 1 < 0:
                        tmp[r][c] = (tmp[r][c] + 1) % mod
                    else:
                        tmp[r][c] = (tmp[r][c] + dp[r - 1][c]) % mod

                    if c + 1 == col:
                        tmp[r][c] = (tmp[r][c] + 1) % mod
                    else:
                        tmp[r][c] = (tmp[r][c] + dp[r][c + 1]) % mod

                    if c - 1 < 0:
                        tmp[r][c] = (tmp[r][c] + 1) % mod
                    else:
                        tmp[r][c] = (tmp[r][c] + dp[r][c - 1]) % mod

            dp = tmp
        return dp[startRow][startColumn]

                    


        '''
        # Memoization -> TLE
        row = m
        col = n
        mod = 10**9+7
        dp = {}

        def dfs(r ,c ,moves):
            if (r < 0 or r == row or c < 0 or c == col):
                return 1

            if moves == 0:
                return 0

            if(r, c, moves) in dp:
                return dp[(r, c, moves)]


            dp[(r, c, moves)] = (
                (dfs(r + 1, c, moves - 1) +
                dfs(r - 1, c, moves - 1)) % mod +
                (dfs(r, c + 1, moves - 1) +
                dfs(r, c - 1, moves - 1)) % mod
            ) % mod

            return dp[(r, c, moves)]

        return dfs(startRow, startColumn, maxMove)
        '''
        
        '''
        # Recursion -> TLE
        row = m
        col = n
        mod = 10**9+7

        def dfs(r ,c ,moves):
            if (r < 0 or r == row or c < 0 or c == col):
                return 1

            if moves == 0:
                return 0

            return (
                (dfs(r + 1, c, moves - 1) +
                dfs(r - 1, c, moves - 1)) % mod +
                (dfs(r, c + 1, moves - 1) +
                dfs(r, c - 1, moves - 1)) % mod
            ) % mod

        return dfs(startRow, startColumn, maxMove)
        '''
            

        '''
        memo = {}
        def rec(r,c,M):
            if (r,c,M) in memo:
                return memo[(r,c,M)]
            
            if(r < 0 or c < 0 or r >= m or c >= n):
                return 1
            
            if M == 0:
                return 0
            
            ans = 0
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                ans += rec(r+x,c+y,M-1)
            memo[(r,c,M)] = ans
            
            return ans
        
        return rec(startRow,startColumn,maxMove)%(10**9+7)

        '''
      
