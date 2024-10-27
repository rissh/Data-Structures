
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        perms = [
            [nums[0], nums[1], nums[2]],
            [nums[0], nums[2], nums[1]],
            [nums[1], nums[0], nums[2]],
            [nums[1], nums[2], nums[0]],
            [nums[2], nums[0], nums[1]],
            [nums[2], nums[1], nums[0]]
        ]
    
        for perm in perms:
            binary = ''.join(format(num, 'b') for num in perm)
            decimal = int(binary, 2)
            res = max(res, decimal)
    
        return res
        
