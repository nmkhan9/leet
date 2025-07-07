# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = head

        while prev and prev.next :
            if prev.val == prev.next.val :
                prev.next = prev.next.next
            else :
                prev = prev.next
        return head
        