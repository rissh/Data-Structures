
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        n = len(arr)
        Charset = set()

        def overlap(Charset, s):
            #c = Counter(Charset) + Counter(s)
            #return max(c.values()) > 1

            prev = set()
            for c in s:
                if c in Charset or c in prev:
                    return True

                prev.add(c)

            return False

        def backtrack(i):
            if i == n:
                return len(Charset)
                
            res = 0
            if not overlap(Charset, arr[i]):
                for c in arr[i]:
                    Charset.add(c)

                res = backtrack(i + 1)
                for c in arr[i]:
                    Charset.remove(c)

            return max(res, backtrack(i + 1))

        return backtrack(0)

