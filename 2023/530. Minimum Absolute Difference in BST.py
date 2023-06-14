# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float("inf")
        val_list = []
        self.inorder(root, val_list)

        for i in range(len(val_list) - 1):
            min_diff = min(min_diff, val_list[i + 1] - val_list[i])

        return min_diff

def inorder(self, node, val_list):
        if node is None:
            return
        else:
            self.inorder(node.left, val_list)
            val_list.append(node.val)
            self.inorder(node.right, val_list)
