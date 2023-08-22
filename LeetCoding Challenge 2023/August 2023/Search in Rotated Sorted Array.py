
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        low = 0
        high = n - 1

        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] == target):
                return mid

            if(nums[mid] >= nums[0]):
                if(target > nums[mid] or target < nums[0]):
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                if(target < nums[mid] or target > nums[n-1]):
                    high = mid - 1
                else:
                    low = mid + 1

        return -1
