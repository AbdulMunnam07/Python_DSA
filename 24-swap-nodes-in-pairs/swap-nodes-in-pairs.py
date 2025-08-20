# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only one node, return it
        if not head or not head.next:
            return head
        
        # The two nodes to be swapped
        first = head
        second = head.next
        
        # Recursively swap the rest of the list starting from second.next
        first.next = self.swapPairs(second.next)
        
        # Swap first and second
        second.next = first
        
        # New head after swap is 'second'
        return second

    

        