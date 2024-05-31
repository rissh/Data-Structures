

def f(nums, i, hashMap, k):

    n = len(nums)
    if i == n:
        return 1

    # Skip nums[i]
    res = f(nums, i + 1, hashMap, k)

    if not hashMap[nums[i] + k] and not hashMap[nums[i] - k]:
        # Include nums[i]
        hashMap[nums[i]] += 1
        res += f(nums, i + 1, hashMap, k)
        hashMap[nums[i]] -= 1

    return res

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        n = len(nums)
        count = defaultdict(int)

        return f(nums, 0, count, k) - 1
        
