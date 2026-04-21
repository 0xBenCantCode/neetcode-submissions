# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: # edge case
            return False

        cache = set() # keep track of nodes in linked list set for O(1)

        pointer = head # probably don't need this

        while head:
            cache.add(head) # add current node to cache,
            if head.next == None:
                return False # no cycle case
            
            if head.next in cache:
                return True
            
            head = head.next # move forward one
