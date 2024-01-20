
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
        n = len(nums)
        BitsCounts = [0] * n

        for j in range(n):
            count = 0
            num = nums[j]
            while num:
                count += num & 1
                num >>= 1
            BitsCounts[j] = count

        k = 0

        while k < n:
            for i in range(1, n):
                if BitsCounts[i] == BitsCounts[i - 1] and nums[i] < nums[i - 1]:
                    nums[i], nums[i - 1] = nums[i - 1], nums[i]

    
            IsSorted = True
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    IsSorted = False
                    break

            if IsSorted:
                return True
            k += 1

        return False
      
