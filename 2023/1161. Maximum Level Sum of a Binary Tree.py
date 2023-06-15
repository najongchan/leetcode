# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_nodes = defaultdict(int)
        node_list = [(1, root)]

        while node_list:
            level, node = node_list.pop()
            level_nodes[level] += node.val
            if node.left is not None:
                node_list.append((level + 1, node.left))
            if node.right is not None:
                node_list.append((level + 1, node.right))

        return max(level_nodes, key=level_nodes.get())

