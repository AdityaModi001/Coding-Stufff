# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # dummynode = ListNode(0)
        # [0  1,  2,  3,  4,  5]
           
        values_to_remove = set(nums)
        
        # n = len(nums)
        # for i in range(n):
        #     value_to_remove = nums[i]
        #     while curr is not None and curr.next is not None:
        #         if value_to_remove == curr.next.val:
        #             curr.next = curr.next.next 
                
        #         curr = curr.next
        #     curr = dummynode.nex
        # second_pointer = head
        # for i in range(n):
        #     value_to_remove = nums[i]
        #     dummynode.next = head  
        #     curr = dummynode
        #     second_pointer = head
        #     while second_pointer is not None:
        #         if value_to_remove != second_pointer.val:
        #             curr.next = second_pointer
        #             curr = second_pointer
        #             second_pointer = second_pointer.next
                    
        #         else:
        #             second_pointer = second_pointer.next
        #     curr.next = None
        #     head = dummynode.next
        # return dummynode.next
        dummy = ListNode(next=head)
        curr = dummy
        while curr.next:
            if curr.next.val in values_to_remove:
                curr.next = curr.next.next
            else:
                curr = curr.next 
            
        return dummy.next