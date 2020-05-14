# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Runtime: 48 ms, faster than 93.53% of Python online submissions for Add Two Numbers.
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
print(s.addTwoNumbers(l1,l2))
