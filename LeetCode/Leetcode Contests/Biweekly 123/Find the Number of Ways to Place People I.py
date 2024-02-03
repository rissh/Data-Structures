
class Solution:
    
    def f(self, point: List[int], top_left: List[int], bottom_right: List[int]) -> bool:
        x = point[0]
        y = point[1]

        X1 = top_left[0]
        Y1 = top_left[1]
        X2 = bottom_right[0]
        Y2 = bottom_right[1]

        if not self.f2(top_left, bottom_right):
            return False

        if X1 <= x <= X2 and Y1 >= y >= Y2:
            return True
        else:
            return False
    
    def f2(self, top_left: List[int], bottom_right: List[int]) -> bool:
        return top_left[0] <= bottom_right[0] and top_left[1] >= bottom_right[1]

    
        
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        hashMap = [(it[0], it[1]) for it in points]
        n = len(hashMap)
        res = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if self.f2(hashMap[i], hashMap[j]):
                    x = 1
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        if self.f(hashMap[k], hashMap[i], hashMap[j]):
                            x = 0
                            break
                    if x:
                        res += 1
        return res
