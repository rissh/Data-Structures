
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        n = len(nums)
        mod = 10 ** 9 + 7

        def rev(num):
            return int(str(num)[::-1])

        total = 0
        hashMap = collections.Counter()

        for x in nums:
            curr = x - rev(x)
            total += hashMap[curr]
            total % mod
            hashMap[curr] += 1

        return total % mod

