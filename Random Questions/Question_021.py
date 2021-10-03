"""GitHub : Alimov - 8"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        head = dummy
        
        while(l1 is not None and l2 is not None):
            if(l1.val <= l2.val):
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
            
        if(l1 is None):
            dummy.next = l2
        else:
            dummy.next = l1
            
        return head.next
        
