# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # keep two pointers, one going twice the speed as the first. 
        # if the faster pointer ever reaches the end, we are done.
        # otherwise, it should reach our slow pointer and we can say there is a cycle
        fast = head
        slow = head
        while (fast):
            fast = fast.next
            if slow == fast:
                return True
            elif not fast:
                return False
            fast = fast.next
            if slow == fast:
                return True
            elif not fast:
                return False
            slow = slow.next
        return False
