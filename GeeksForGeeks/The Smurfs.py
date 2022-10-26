
#User function Template for python3

class Solution:
    def minFind(self, n, a):
        # code here
        Red, Green, Blue = 0, 0, 0
        for color in a:
            if color == 'R': Red += 1
            elif color == 'G': Green += 1
            elif color == 'B': Blue += 1
        if (Red%2 == 0 and Green%2 == 0 and Blue%2 == 0) or (Red%2 != 0 and Green%2 != 0 and Blue%2 != 0): return 2
        return 1
      
