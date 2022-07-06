
#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def diagonal(self,root):
        ans=[]
        st=deque([root])
        while st:
            n=len(st)
            while n>0:
                n-=1
                node=st.popleft()
                while node:
                    ans.append(node.data)
                    if node.left:
                        st.append(node.left)
                    node=node.right
        return ans
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        #code here
        
