# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node and set current to that node
        dummy = ListNode()
        current = dummy

        # set the next of current node to the smaller value of two lists; iterate through lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        # once one list is empty, attach remaining nodes of other list
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # return next of dummy node (head of merged list)
        return dummy.next