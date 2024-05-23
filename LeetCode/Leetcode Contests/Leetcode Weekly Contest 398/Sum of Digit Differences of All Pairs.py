
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        
        n = len(nums)
        digit = len(str(nums[0]))
        total = 0
    
        for position in range(digit):
            count = [0] * 10
            
            for num in nums:
                digit = (num // 10 ** position) % 10
                count[digit] += 1
                
            for digit in range(10):
                pairs_count = count[digit] * (n - count[digit])
                total += pairs_count
    
        return total // 2

