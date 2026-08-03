# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        k = 0
        temp = head
        while temp:
            k += 1
            temp = temp.next
        n1 = k - n
        if n1 == 0:
            return head.next
        prev = None
        curr = head
        i = 0
        while curr:
            if i == n1:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
            i += 1
        return head