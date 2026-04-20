# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 -> 2 -> 3 -> 4
        # 1 <- 2 <- 3 <- 4
        previous = None
        while head:

            nextLink = head.next
            head.next = previous

            previous = head
            head = nextLink # progress initial list
        
        return previous