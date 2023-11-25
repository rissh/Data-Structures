
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        # tc --> O(n * m * log n)
        # sc --> O(n + m)
        n = len(nums)
        m = len(l)

        ans = []
        for start,end in zip(l,r):
            ans.append(True)
            curr = sorted(nums[start:end+1])

            diff = curr[1] - curr[0]
            for i in range(1, len(curr)):
                if curr[i] - curr[i -1] != diff:
                    ans[-1] = False

        return ans
      
