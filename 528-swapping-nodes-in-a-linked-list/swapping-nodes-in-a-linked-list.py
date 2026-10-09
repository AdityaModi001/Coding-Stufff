import sys
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # dummyNode = ListNode(0)
        # dummyNode.next = head 
        # curr = dummyNode
        


        curr = head 
        total_nodes_count = 0 
        while curr is not None:
            total_nodes_count += 1 
            curr = curr.next
        print(total_nodes_count)

        to_swap_idx1 = k 
        to_swap_idx2 = total_nodes_count - k + 1
        if to_swap_idx1 == to_swap_idx2:
            return head 

        curr = head 
        for i in range(1,total_nodes_count+1):
            if i == to_swap_idx1:
                first_node = curr
        
            elif i == to_swap_idx2:
                second_node = curr 
            curr = curr.next
        
        print(first_node.val)
        print(second_node.val)
        
        total_nodes_count += 1

        to_swap_idx1 = k - 1
        to_swap_idx2 = total_nodes_count - k 

        # dummynode = ListNode(0)
        # dummynode.next = head

        # curr = dummynode 
        # for i in range(total_nodes_count):
        #     if i == to_swap_idx1:
        #         print(i)
        #         curr.next = second_node
        #         second_node.next = curr.next.next
        #     elif i == to_swap_idx2:
        #         curr.next = first_node
        #         first_node.next = curr.next.next
        #     curr = curr.next 

        first_node.val, second_node.val = second_node.val , first_node.val
    
        return head