
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        nums = word.upper()
        if(nums == word):
            return True

        nums = word.lower()
        if(nums == word):
            return True

        nums = word.capitalize()
        if(nums == word):
            return True

        return False
      
