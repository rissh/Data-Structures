
#User function Template for python3

'''
#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
#Tree Node        
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None
'''

class Solution:
   def sortedListToBST(self, head):
       #code here
       if head == None:
           return head
       if head.next == None:
           temp = TNode(head.data)
           return temp
       prev, mid = self.middle(head)
       prev.next = None
       nxt = mid.next
       mid.next = None
       root = TNode(mid.data)
       root.left = self.sortedListToBST(head)
       root.right = self.sortedListToBST(nxt)
       return root
   
   def middle(self, head):
       prev = None
       slow = head
       fast = head
       while fast and fast.next:
           prev = slow
           slow = slow.next
           fast = fast.next.next
       return prev, slow
    
