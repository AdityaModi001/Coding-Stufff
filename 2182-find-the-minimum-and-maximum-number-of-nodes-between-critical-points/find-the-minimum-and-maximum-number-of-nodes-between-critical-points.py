# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """

        curr = head 
        if curr.next.next is None:
            return [-1,-1]


        prev_node = curr
        curr = curr.next
        next_node = curr.next

        res = []
        count = 1
        while curr.next is not None:
            count += 1
            if curr.val > prev_node.val and curr.val > next_node.val:
                res.append(count)
                
            if curr.val < prev_node.val and curr.val < next_node.val:
                res.append(count)

            prev_node = curr
            curr = curr.next
            next_node = curr.next
        
        if len(res) <= 1:
            return [-1,-1]
        min_distance = float('inf')
        for i in range(1,len(res)):
            if res[i] - res[i-1] < min_distance:
                min_distance  = res[i] - res[i-1]
        
        max_disctance = res[-1] - res[0]
        return [min_distance,max_disctance]

        