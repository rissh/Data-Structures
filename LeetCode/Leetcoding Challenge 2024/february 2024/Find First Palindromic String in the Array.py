
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for num in words:
            
            if num == num[::-1]:
                return num

        return "" 
