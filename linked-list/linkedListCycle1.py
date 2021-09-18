# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return False
        slow = head
        fast = head.next
        while slow and fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
        return slow==fast
        