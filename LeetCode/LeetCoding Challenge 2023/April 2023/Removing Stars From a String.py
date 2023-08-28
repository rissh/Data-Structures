
class Solution:
    def removeStars(self, s: str) -> str:

        n = len(s)
        stack = []

        for char in s:
            if char  == "*":
                stack and stack.pop()

            else:
                stack.append(char)

        return "".join(stack)
      
