"""
Title: Preorder traversal

Problem:
    Given a binary tree, return the preorder traversal of its nodes' values.

Execution: python preorder_traversal.py
"""
from typing import List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    stack = [root]
    visited = []
    out = []
    while stack:
        node = stack[-1]
        if node and node not in visited:
            out.append(node.val)
            visited.append(node)
        if node.left and node.left not in visited:
            stack.append(node.left)
            continue
        if node.right and node.right not in visited:
            stack.append(node.right)
            continue
        stack.pop()
    return out

    def traverse(root, out, visited):
        if root:
            out = traverse(root.left, out, visited)
            if root not in visited:
                visited.append(root)
                out.append(root.val)
            out = traverse(root.right, out, visited)
        return out

    return traverse(root, [], [])


class TestInorderTraversal(unittest.TestCase):
    """Unit tests for inorder_traversal."""

    def test_1(self):
        tn = TreeNode(1)
        tn.right = TreeNode(2)
        tn.right.left = TreeNode(3)
        self.assertEqual(preorder_traversal(tn), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
