
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def f(num):

            count = bin(num).count('1')
            return (count, num)

     
        arr.sort(key=f)
        return arr
      
