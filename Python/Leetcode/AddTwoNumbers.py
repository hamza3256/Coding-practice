# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        v = c = 0
        ptr = a = ListNode(-1)
        while l1 or l2 or c > 0:
            if l1 and l2:
                v = l1.val + l2.val+c
                if v<10:
                    ptr.next = ListNode(v)
                    c = 0
                else:
                    ptr.next = ListNode(v-10)
                    c = 1
                ptr = ptr.next
                l1 = l1.next; l2 = l2.next
            else:
                if l2:
                    v = l2.val+c
                    if v<10:
                        ptr.next = ListNode(v)
                        c = 0
                    else:
                        ptr.next = ListNode(v-10)
                        c = 1
                    l2 = l2.next; ptr = ptr.next
                    
                elif l1:
                    v = l1.val+c
                    if v < 10:
                        ptr.next = ListNode(v)
                        c = 0
                    else:
                        ptr.next = ListNode(v-10)
                        c = 1
                    l1 = l1.next; ptr = ptr.next
                else:
                    ptr.next = ListNode(c)
                    c = 0
                    ptr = ptr.next
        return a.next