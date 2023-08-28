
class Solution:
    def nsr(self, nums):
        n = len(nums)
        stack, index, res = [], [], []
        i = len(nums)-1
        while i >= 0:
            if len(stack) == 0:
                res.append(n-i)
            elif len(stack) > 0 and stack[-1] < nums[i]:
                res.append(index[-1]-i)
            elif len(stack) > 0 and stack[-1] >= nums[i]:
                stack.pop()
                index.pop()
                while len(stack) > 0 and stack[-1] >= nums[i]:
                    stack.pop()
                    index.pop()
                if len(stack) == 0:
                    res.append(n-i)
                elif len(stack) > 0 and stack[-1] < nums[i]:
                    res.append(index[-1]-i)
            stack.append(nums[i])
            index.append(i)
            i = i-1
        return res[::-1]
    
    def nsl(self, nums):
        temp = -1
        stack, index, res = [], [], []
        for i in range(len(nums)):
            if len(stack) == 0:
                res.append(i-temp)
            elif len(stack) > 0 and stack[-1] <= nums[i]:
                res.append(i-index[-1])
            elif len(stack) > 0 and stack[-1] > nums[i]:
                stack.pop()
                index.pop()
                while len(stack) > 0 and stack[-1] > nums[i]:
                    stack.pop()
                    index.pop()
                if len(stack) == 0:
                    res.append(i-temp)
                elif len(stack) > 0 and stack[-1] <= nums[i]:
                    res.append(i-index[-1])
            stack.append(nums[i])
            index.append(i)
        return res
                    
    
    def sumSubarrayMins(self, arr: List[int]) -> int:
        right = self.nsr(arr)
        left = self.nsl(arr)
        #print(left, right)
        ans = 0
        for i in range(len(arr)):
            ans += (left[i]*right[i]*arr[i])
        return ans% (10**9 + 7)
        
