
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        n = len(num)

        s = [str(i) for i in num]
        res = int("".join(s))

        ans = res + k
        nums = [int(x) for x in str(ans)]

        return nums
        
