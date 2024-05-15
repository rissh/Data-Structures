
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        
        n = len(points)
        for i in range(n):
            points[i][0] = abs(points[i][0])
            points[i][1] = abs(points[i][1])

        l = 0
        r = int(1e9)
        res = 0

        while l <= r:
            mid = (l + r) // 2
            m = {}
            f = 1

            for i in range(n):
                if points[i][0] <= mid and points[i][1] <= mid:
                    c = s[i]
                    m[c] = m.get(c, 0) + 1

            for val in m.values():
                if val > 1:
                    f = 0
                    break

            if f == 1:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        count = 0
        for i in range(n):
            if points[i][0] <= res and points[i][1] <= res:
                count += 1

        return count
        
