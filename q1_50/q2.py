# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time: O(max(M, N))
    # Space: O(1)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None: 
            return l2 
        if l2 is None: 
            return l1 

        dummy = ListNode(0)
        cur = dummy 
        carry = 0 
        while (l1 is not None) or (l2 is not None) or carry != 0: 
            cur_sum = carry 
            if l1 is not None: 
                cur_sum += l1.val 
                l1 = l1.next 
            if l2 is not None: 
                cur_sum += l2.val 
                l2 = l2.next 

            cur.next = ListNode(cur_sum % 10)
            cur = cur.next 
            carry = cur_sum // 10 

        return dummy.next 
