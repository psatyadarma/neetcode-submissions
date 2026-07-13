# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root, root.val)]
        while stack:
            root, max_so_far = stack.pop()
            if root.val >= max_so_far:
                count += 1
            max_so_far = max(max_so_far, root.val)
            if root.left:
                stack.append((root.left, max_so_far))
            if root.right:
                stack.append((root.right, max_so_far))
        return count
