
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        n = len(nums)
        count = defaultdict(int)
        res = 0
        left = 0

        for right in range(n):
            count[nums[right]] += 1
            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1
                
            res = max( res, right - left + 1)

        return res
        '''
        n = len(nums)
        freq = Counter()
        left = 0
        res = 0

        for right in range(n):
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
        '''
        
