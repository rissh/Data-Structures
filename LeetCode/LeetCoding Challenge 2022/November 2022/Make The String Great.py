
class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        for i in s:
            if len(st) == 0:
                st.append(i)
            else:
                if st[-1].lower() == i.lower() and st[-1] != i:
                    st.pop()
                else:
                    st.append(i)
                    
        # print(st)
        return "".join(st)
        
# Method 2
class Solution:
    def makeGood(self, s: str) -> str:
        diff = abs(ord('a') - ord('A'))
        stack = []
        for c in s:
            if stack and abs(ord(c) - ord(stack[-1])) == diff:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
