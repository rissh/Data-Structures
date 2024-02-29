
class Solution:
    def frequencySort(self, s: str) -> str:

        n = len(s)
        hashMap = Counter(s)
        bucket = defaultdict(list)

        for char, cnt in hashMap.items():
            bucket[cnt].append(char)

        res = []
        for i in range(n, 0, -1):
            for c in bucket[i]:
                res.append(c * i)

        return "".join(res)
      
