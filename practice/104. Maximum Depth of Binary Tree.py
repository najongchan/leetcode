# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isLeaf(self, node):
        if node.left == None and node.right == None:
            return True
        else:
            return False
    
    def recursionDepth(self, node):
        if node == None:
            return 0
        if self.isLeaf(node):
            return 1
        
        return max(self.recursionDepth(node.left), self.recursionDepth(node.right)) + 1
    
    def maxDepth(self, root: TreeNode) -> int:
        # print(root)
        return self.recursionDepth(root)