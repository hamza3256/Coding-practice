# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        l3 = ptr = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    ptr.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    ptr.next = ListNode(l2.val)
                    l2 = l2.next
                ptr = ptr.next
            else:
                if not l1:
                    ptr.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    ptr.next = ListNode(l1.val)
                    l1 = l1.next
                ptr = ptr.next
        return l3.next            