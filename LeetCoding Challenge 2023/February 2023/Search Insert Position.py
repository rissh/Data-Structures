
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
				
		# target value not present ->
        if(target not in nums):
            nums.append(target)

        sortNums = sorted(nums)
        return sortNums.index(target)
        
