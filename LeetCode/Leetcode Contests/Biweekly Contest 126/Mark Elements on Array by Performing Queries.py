
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        n = len(nums)
        markInd = set()
        res = []

        unmarkHeap = []
        for i in range(n):
            if i not in markInd:
                unmarkHeap.append((nums[i], i))
        heapq.heapify(unmarkHeap)

        total = sum(nums) - sum(nums[i] for i in markInd)

        for query in queries:
            ind, k = query
            if ind not in markInd:
                markInd.add(ind)
                total -= nums[ind]

            remaining_k = k
            while remaining_k > 0 and unmarkHeap:
                value, index = heapq.heappop(unmarkHeap)
                if index not in markInd:
                    markInd.add(index)
                    total -= value
                    remaining_k -= 1

            res.append(total)

        return res
        
