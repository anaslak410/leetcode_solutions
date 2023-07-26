# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []

        self.traverse(root, k)
        print(self.arr)
        return self.arr[(k-1)]

    def traverse(self, root, k):
        if root is None:
            return

        self.traverse(root.left, k)
        self.arr.append(root.val)
        self.traverse(root.right, k)
