
class Solution:
    def pivotInteger(self, n: int) -> int:

        totalSum = n * (n + 1) // 2
        for i in range(n + 1):
            leftSum = i * (i + 1) // 2
            rightSum = totalSum - leftSum + i

            if leftSum == rightSum:
                return i

        return -1



        '''
        totalSum = n * (n + 1) // 2
        for i in range(n + 1):
            leftSum = i * (i + 1) // 2

            if leftSum == totalSum - leftSum + i:
                return i

        return -1
        '''
      
