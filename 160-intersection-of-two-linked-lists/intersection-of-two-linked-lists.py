# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []

        curr1, curr2 = headA, headB

        while curr1 is not None:
            stack1.append(curr1)
            curr1 = curr1.next

        while curr2 is not None:
            stack2.append(curr2)
            curr2 = curr2.next

        intersection_node = None

        while stack1 and stack2:
            e1 = stack1.pop()
            e2 = stack2.pop()

            if e1 == e2:
                intersection_node  = e1
            else:
                break

        return intersection_node

