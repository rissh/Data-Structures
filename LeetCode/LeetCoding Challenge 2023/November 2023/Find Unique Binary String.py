
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        strSet = {s for s in nums}
        n = len(nums)
        m = len(nums[0])

        def back(i, curr):
            if i == n:
                res = "".join(curr)
                return None if res in strSet else res

            res = back(i + 1, curr)
            if res:
                return res
            curr[i] = "1"
            res = back(i + 1, curr)
            if res:
                return res

        return back(0, ["0" for s in nums])
      
