# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None and head.next is None:
            return head
        
        dummynode = ListNode(None)
        dummynode.next = head 
        curr = head 
        count = 0 
        while curr is not None:
            count += 1
            curr = curr.next 

        to_remove = count - n
        curr = dummynode
        for _ in range(to_remove):
            curr = curr.next 

        curr.next = curr.next.next 

        return dummynode.next