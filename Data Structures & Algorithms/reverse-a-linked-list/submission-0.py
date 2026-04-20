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
        currentLink = head
        while currentLink:

            nextLink = currentLink.next
            currentLink.next = previous

            previous = currentLink
            currentLink = nextLink
        
        return previous