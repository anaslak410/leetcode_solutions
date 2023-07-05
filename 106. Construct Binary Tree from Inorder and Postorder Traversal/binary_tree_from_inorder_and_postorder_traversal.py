# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]

    
"""
- inorder prints left subtree, then value, then right subtree
- postorder prints left subtree, then right subtree, then value
- must account for missing subtrees
- last item in postorder is the root
- if left subtree is null
    - both inord and postord print left then root
- if right subtree is null
    - inord prints value then right subtree, postorder prints right subtree then value



"""

if __name__ == "__main__":
    s = Solution()
    s.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3])
