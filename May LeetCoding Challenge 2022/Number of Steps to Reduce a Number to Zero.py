
class Solution:
    def numberOfSteps(self, num: int,steps=0) -> int:
        if(num == 0):
            return steps
        if num % 2 == 0:
            return self.numberOfSteps(num // 2, steps+1)
        else:
            return self.numberOfSteps(num - 1, steps+1)
          
