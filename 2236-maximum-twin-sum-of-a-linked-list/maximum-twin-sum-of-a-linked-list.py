# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        twin_sum = []
        stack = []
        curr = head 
        count = 0 
        while curr is not None:
            stack.append(curr)
            count += 1
            curr = curr.next 
        
        mid = (count//2) 
        curr = head 
        for i in range(mid):
            e = stack.pop()
            value  = curr.val + e.val
            twin_sum.append(value)
            curr = curr.next

        return max(twin_sum)
        