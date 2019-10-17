# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged = ListNode(-1)
        head = merged

        while True:
            if l1 == None:
                merged.next = l2
                break
            
            if l2 == None:
                merged.next = l1
                break

            if l1.val < l2.val:
                if merged.val == -1:
                    merged.val = l1.val
                else:
                    merged.next = ListNode(l1.val)
                    merged = merged.next
                l1 = l1.next
            else:
                if merged.val == -1:
                    merged.val = l1
                else:
                    merged.next = ListNode(l2.val)
                    merged = merged.next
                l2 = l2.next
        return merged