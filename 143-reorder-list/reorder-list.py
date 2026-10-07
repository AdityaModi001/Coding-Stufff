import sys 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head 
            
        stack = []
        curr = head 
        while curr is not None:
            stack.append(curr)
            curr = curr.next 
        
        # Bug 2 Fix: Safely get the midpoint using stack length
        count = len(stack) // 2
        curr = head 
        
        for _ in range(count):
            e = stack.pop()
            next_node = curr.next 
            curr.next = e
            e.next = next_node
            curr = next_node
            
        # Sever the remaining links to prevent cyclic loops
        curr.next = None
        return head


            