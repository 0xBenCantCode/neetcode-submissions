# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        # 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0
        # 0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3

        # 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6

        # 0 -> slow_1 -> fast_2 -> 3 -> 6 -> 5 -> 4

        # alternate after half-reversal

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next


        # reverse half
        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # had to look this part up
        first, second = head, prev
        # pointers to both lists

        while second:
            # 1. Save the next nodes so we don't lose them
            tmp1 = first.next
            tmp2 = second.next
            
            # 2. Re-wire the connections
            first.next = second # head.next = first of second list
            second.next = tmp1 # second list next is first list next
            
            # 3. Move the pointers forward for the next iteration
            first = tmp1
            second = tmp2