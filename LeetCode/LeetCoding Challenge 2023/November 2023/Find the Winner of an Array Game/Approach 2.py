
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
      res = arr[0]
      n = len(arr)
      count = 0

      for i in range(1,n):
          if arr[i] > res:
              res = arr[i]
              count = 0

          count += 1
          if count == k:
              break

      return res
