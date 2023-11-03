
#User function Template for python3
class Solution:
    def checkTriplet(self, arr, n):
        
        square_map = {i * i: i for i in arr}

        for square1 in square_map:
            for square2 in square_map:
           
                sum_of_squares = square1 + square2

                if sum_of_squares in square_map:
                    return True

        return False
      
