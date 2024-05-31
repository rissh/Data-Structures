
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        n = len(nums)
        delta = [(n ^ k) - n for n in nums]
        delta.sort(reverse=True)
        res = sum(nums)

        for i in range(0, n, 2):
            
            if i == n - 1:
                break

            pathDelta = delta[i] + delta[i + 1]
            if pathDelta <= 0:
                break

            res += pathDelta

        return res
      
