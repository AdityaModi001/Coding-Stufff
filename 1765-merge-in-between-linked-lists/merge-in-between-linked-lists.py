# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        curr1 = list1 
        curr2 = list2
        head2 = list1
        for _ in range(b):
            head2 = head2.next
        to_add = head2.next
        for _ in range(a-1):
            curr1 = curr1.next 
        curr1.next = list2
        
        head1 = list1 
        while head1.next is not None:
            head1 = head1.next
        
        head1.next = to_add

        return list1


        
            

        
        

        


            