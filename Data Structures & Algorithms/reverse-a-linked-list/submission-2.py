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
            nextLink = head.next # pointer to next link
            head.next = previous # out next link will be equal to the previous link. None = tail

            previous = head # previous is now equal to og list, where the tail is now null and the head is 1
            head = nextLink # progress initial list head to the next link
        return previous