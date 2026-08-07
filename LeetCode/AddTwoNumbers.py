# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1 = 0
        val2 = 0
        i = 1
        while l1 != None:
            val1 += l1.val * i
            l1 = l1.next
            i *= 10
        i = 1
        while l2 != None:
            val2 += l2.val * i
            l2 = l2.next
            i *= 10
        
        _sum = val1 + val2
        if _sum == 0:
            return ListNode()
        head = None
        current = None
        while _sum > 0:
            value_to_append = _sum % 10
            new_node = ListNode(value_to_append)

            if head is None:
                head = new_node
                current = head
            else:
                current.next = new_node
                current = new_node
            
            _sum //= 10
        
    
        return head


#     # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy=ListNode(-1)
#         current=dummy
#         carry=0
#         while l1 is not None or l2 is not None:
#             total=carry
#             if l1 is not None:
#                 total+=l1.val
#                 l1=l1.next
#             if l2 is not None:
#                 total+=l2.val
#                 l2=l2.next
#             digit=total%10
#             carry=total//10

#             current.next=ListNode(digit)
#             current=current.next
#         if carry==1:
#             current.next=ListNode(1)
#             current=current.next

#         return dummy.next
        