class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head

        #del from start
        while head != None and head.val == val:
            head = head.next
        
        if head == None:
            return None

        temp = head
        while temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next

            else:
                temp = temp.next

        return head
