
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        hashMap = defaultdict(int)
        n = len(paths)

        for A, B in paths:
            hashMap[A] += 1
            hashMap[B] += 0

        for x in hashMap.keys():
            if hashMap[x] == 0:
                return x

        return ""
      
