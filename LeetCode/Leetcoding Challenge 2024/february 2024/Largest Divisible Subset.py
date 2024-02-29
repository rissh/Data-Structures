
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        nums.sort()

        n = len(nums)
        path = [-1] * n
        counts = [1] * n
        last_index = 0
        
        for i in range(n):
            for prev in reversed(range(i)):
                if nums[i] % nums[prev] == 0 and counts[prev] + 1 > counts[i]:
                    counts[i] = counts[prev] + 1
                    path[i] = prev
                    if counts[last_index] < counts[i]:
                        last_index = i

        subset = []
        while last_index != -1:
            subset.append(nums[last_index])
            last_index = path[last_index]
        
        return subset
      
