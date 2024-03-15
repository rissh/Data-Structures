
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        hashMap = defaultdict(int)
        count = 0

        for c in order:
            hashMap[c] = count
            count += 1

        #return "".join(sorted(str,key=lambda x:hashMap[x]))
        return "".join(sorted(s,key=order.find))
      
