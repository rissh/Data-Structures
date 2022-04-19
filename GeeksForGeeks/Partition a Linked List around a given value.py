
class Solution:
    def partition(self, head, x):
        #code here
        small=Node(-999)
        big=Node(99)
        s=small
        b=big
        equal=Node(x)
        e=equal
        root=head
        while root is not None:
            
                
            if root.data<x:
                small.next=Node(root.data)
                small=small.next
            elif root.data>x:
                
                big.next=Node(root.data)
                big=big.next
                
            else:
                equal.next=Node(root.data)
                equal=equal.next
            root=root.next
        
        
        equal.next=b.next
        small.next=e.next
        
        return s.next
      
