
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        res = 0
        prevRes = defaultdict(int)

        for num in nums:
            currRes = defaultdict(int)

            if num == k:
                res += 1
            currRes[num] += 1

            for val, freq in prevRes.items():
                new = val & num
                if new == k:
                    res += freq
                currRes[new] += freq
            
            prevRes = currRes
        
        return res

