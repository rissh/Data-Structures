
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        n = len(nums)
        FirstMin = second_min = 51
        ind = 1

        while ind < n:
            curr = nums[ind]

            if curr < FirstMin:
                SecMin = FirstMin
                FirstMin = curr
                
            elif curr < SecMin:
                SecMin = curr

            ind += 1

        return nums[0] + FirstMin + SecMin
      
