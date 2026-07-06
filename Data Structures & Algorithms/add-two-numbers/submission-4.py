# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head1, head2 = l1, l2
        newHead = ListNode()
        head = newHead
        while head1 and head2:
            plus = int(head1.val) + int(head2.val) + carry
            if plus >= 10:
                carry = 1
                plus = plus - 10
            else:
                carry = 0
            head.next = ListNode(plus)
            head = head.next
            head1 = head1.next
            head2 = head2.next
        while head1:
            plus = int(head1.val) + carry
            if plus >= 10:
                carry = 1
                plus = plus - 10
            else:
                carry = 0
            head.next = ListNode(plus)
            head = head.next
            head1 = head1.next
        while head2:
            plus = int(head2.val) + carry
            if plus >= 10:
                carry = 1
                plus = plus - 10
            else:
                carry = 0
            head.next = ListNode(plus)
            head = head.next
            head2 = head2.next
        if carry > 0:
            head.next = ListNode(carry)
        return newHead.next
        
