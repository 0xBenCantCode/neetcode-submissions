# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # create new linked list to store merged.
        finalList = ListNode(0)
        pointerFinalList = finalList

        while list1 and list2:
            if list1.val <= list2.val:
                pointerFinalList.next = list1
                list1 = list1.next # +1
            else:
                pointerFinalList.next = list2
                list2 = list2.next

            pointerFinalList = pointerFinalList.next # move pointer one

        pointerFinalList.next = list1 or list2 # add on remaining links (points to actual finalList so ok)
        return finalList.next # skip first