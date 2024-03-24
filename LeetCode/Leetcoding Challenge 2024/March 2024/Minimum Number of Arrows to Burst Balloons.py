
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        n = len(points)
        res = n
        points.sort()
        
        prev = points[0]
        for i in range(1, n):
            curr = points[i]

            if curr[0] <= prev[1]:
                res -= 1
                prev = [curr[0], min(curr[1], prev[1])]

            else:
                prev = curr

        return res

        '''
        points = sorted(points)
        p = points[0][0]
        q = points[0][1]
        ans = 0

        for i,j in points:
            
            if p <= i <= q or p <= j <= q:
                p = max(i,p)
                q = min(j,q)

            else:
                ans += 1
                p = i
                q = j

        return ans + 1
        '''
      
