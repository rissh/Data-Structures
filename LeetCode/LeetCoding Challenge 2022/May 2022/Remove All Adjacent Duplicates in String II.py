
# Method 1
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c,1])
            
            if stack[-1][1] == k:
                stack.pop()
        res = ""
        for char,count in stack:
            res += (char*count)
        return res
      
# Method 2
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        ans = []
        for i in range(len(s)):
            if not ans or ans[-1][0] != s[i]:
                ans.append([s[i], 1])
            elif ans[-1][0] == s[i]:
                ans[-1][1] += 1
            if ans[-1][1] == k:
                ans.pop()
        
        return "".join(p[0] * p[1] for p in ans)
