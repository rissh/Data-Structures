
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        prev = [0] * (m + 1)

        for i in range(n):
            dp = [0] * (m + 1)

            for j in range(m):

                if nums1[i] == nums2[j]:
                    dp[j + 1] = 1 + prev[j]
                    
                else:
                    dp[j + 1] = max(dp[j], prev[j + 1])

            prev = dp

        return prev[m]
        
