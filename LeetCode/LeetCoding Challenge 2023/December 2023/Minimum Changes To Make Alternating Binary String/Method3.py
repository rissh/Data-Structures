
class Solution:
    def minOperations(self, s: str) -> int:

      count0 = count1 = 0 

      for ind, x in enumerate(s):
          if ind % 2 == int(x):
            count0 +=1
          else:
            count1 += 1

      return min(count0, count1)
