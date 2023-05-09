# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        header = ListNode(0)
        header.next = head
        
        current_node = header
        limit_node = header

        for _ in range(n+1):
            current_node = current_node.next
            print(current_node)

        while current_node != None:
            current_node = current_node.next
            limit_node = limit_node.next
            print(current_node)
            print(limit_node)
        limit_node.next = limit_node.next.next

        return header.next