# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        dummynode = ListNode(0) # 0 
        curr1 = dummynode # 0
        val = 0 
        curr = curr.next
        while curr != None:
            if curr.val != 0:
                val += curr.val
            else:
                dummynode1 = ListNode(val)
                curr1.next = dummynode1
                val = 0 
                curr1 = curr1.next
            curr = curr.next
    
        return dummynode.next
        

        
            
        #     else:
        #         dummynode.next = ListNode(0)
        #     curr = curr.next 
        
        # return dummynode.next

            