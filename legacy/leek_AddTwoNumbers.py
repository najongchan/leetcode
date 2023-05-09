# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nodeToNumber(self, listNode) -> int:
        i = 1
        result_num = 0
        node = listNode
        while node != None:
            result_num += (node.val * i)
            i *= 10
            node = node.next
            
        return result_num
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.nodeToNumber(l1)
        num2 = self.nodeToNumber(l2)

        sum_num = num1 + num2

        node = ListNode(sum_num % 10)
        sum_num = sum_num // 10
        cur_pos = node
        while sum_num > 0:
            cur_pos.next = ListNode(sum_num % 10)
            sum_num = sum_num // 10
            cur_pos = cur_pos.next
        return node