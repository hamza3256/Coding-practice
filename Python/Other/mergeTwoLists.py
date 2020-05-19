# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# faster than 99.58% of online submissions
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

# first attempt — faster than 65 - 68 % of online submissions
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        ptr = l1; ptr2 = l2;
        if ptr.val < ptr2.val:
            a = ListNode(ptr.val)
            ptr = ptr.next
        else:
            a = ListNode(ptr2.val)
            ptr2 = ptr2.next
        ptr3 = a
        while ptr != None and ptr2 != None:
            if ptr.val < ptr2.val:
                ptr3.next = ListNode(ptr.val)
                ptr = ptr.next
                ptr3 = ptr3.next
            elif ptr.val > ptr2.val:
                ptr3.next = ListNode(ptr2.val)
                ptr2 = ptr2.next
                ptr3 = ptr3.next
            else:
                ptr3.next = ListNode(ptr.val);ptr3 = ptr3.next
                ptr3.next = ListNode(ptr.val);ptr3 = ptr3.next
                ptr = ptr.next; ptr2 = ptr2.next
        if ptr == None:
            while ptr2.next != None:
                ptr3.next = ListNode(ptr2.val)
                ptr2 = ptr2.next; ptr3 = ptr3.next
        else:
            while ptr.next != None:
                ptr3.next = ListNode(ptr.val)
                ptr = ptr.next; ptr3 = ptr3.next
        return a

'''

a = [1,2,4]
b = [1,3,4]

l1 = ptr = ListNode(a[0])
for i in range(1,len(a)):
    ptr.next = ListNode(a[i])
    ptr = ptr.next

l2 = ptr = ListNode(b[0])
for i in range(1,len(b)):
    ptr.next = ListNode(b[i])
    ptr = ptr.next

s = Solution()
print(s.mergeTwoLists(l1,l2))
