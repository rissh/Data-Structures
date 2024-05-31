
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        n = len(nums)

        def dfs(i, total):
            
            if i == n:
                return total

            # Pick nums[i] &&  Not Pick nums[i]
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)   

        return dfs(0, 0)
        
