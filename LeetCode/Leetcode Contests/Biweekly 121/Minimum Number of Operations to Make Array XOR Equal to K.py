
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        Xor = 0
        for num in nums:
            Xor ^= num

        target = Xor ^ k
        operations = 0

        while target:
        
            operations += target & 1
            target >>= 1

        return operations
      
