# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head 
        count = 0
        while curr != None:
            curr = curr.next 
            count += 1
        if count == n:
            return head.next

        lenght = count - n - 1
        curr = head 
        for i in range(lenght):
            curr = curr.next 
        curr.next = curr.next.next
        return head


        
