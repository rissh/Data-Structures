
class Solution:
    def partitionString(self, s: str) -> int:

        Hashset = set()
        res = 1

        for char in s:
            if char in Hashset:
                res += 1
                Hashset = set()

            Hashset.add(char)

        return res
        
