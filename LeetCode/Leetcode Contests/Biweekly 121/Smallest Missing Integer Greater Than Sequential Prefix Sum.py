
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        n = len(nums)

        currSum = nums[0]
        i = 1

        while i < n:
            if nums[i] == nums[i - 1] + 1:
                currSum += nums[i]
                i += 1
            else:
                break

        while currSum in count:
            currSum += 1

        return currSum
      
