
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:

        res = ""

        while columnNumber:

            offSet = (columnNumber - 1) % 26
            res += chr(ord("A") + offSet)
            columnNumber = (columnNumber - 1) // 26

        return res[::-1]
      
