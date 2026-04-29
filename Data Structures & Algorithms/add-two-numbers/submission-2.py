# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumVal = l1.val + l2.val
        carry = sumVal // 10
        newList = ListNode(sumVal % 10)
        current = newList
        l1, l2 = l1.next, l2.next
        while(l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sumVal = carry + val1 + val2
            carry = sumVal // 10
            
            current.next = ListNode(sumVal % 10)            
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if(carry > 0):
            current.next = ListNode(carry)   
        return newList
        