# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right, counter = head, head, 1
        doable = False
        current = left.next
        while right.next is not None:
            right = right.next
            counter += 1
            print()
            if counter % k == 0:
                while left != right:
                    temp = current.next
                    current.next = left
                    left = current
                    current = temp
                print(head)
        return head


