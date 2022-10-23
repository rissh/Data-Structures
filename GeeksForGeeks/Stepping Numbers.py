#User function Template for python3
from collections import deque

class Solution:
    def steppingNumbers(self, n, m):
        # code here
        def bfs(n,m, num):
            count = 0
            q = deque()
            q.append(num)
            while q:
                step = q.popleft()
                if step >= n and step <= m:
                    count += 1
                if num == 0 or step > m:
                    continue
                
                lastDigit = step % 10
                step1 = step*10 + (lastDigit - 1)
                step2 = step*10 + (lastDigit + 1)
                
                if lastDigit != 9:
                    q.append(step2)
                if lastDigit != 0:
                    q.append(step1)
                    
            return count
            
        ans = 0
        for i in range(10):
            ans += bfs(n, m, i)
            
        return ans
