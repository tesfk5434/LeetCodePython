# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Status Completed
#Time Complexity: O(N), Beats 100.00 %
#Space Complexity: O(N), Beats 36.23 %

#Sum each node, and useing a variable to hold on to carried digits.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root=ListNode()
        node = root
        carry=0
        while (l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            node.next = ListNode((val1+val2+carry)%10)
            node=node.next
            carry = ((val1+val2+carry)//10)
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            node.next=ListNode(carry)
        return root.next