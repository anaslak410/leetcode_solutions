# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]):
        return self.createNode(postorder, inorder, -1, len(postorder))

    def createNode(self, postorder, inorder, start, finish):
        print("creating node", start, finish)
        root = None

        if (start+1 >= finish):
            print("rejected", start, finish)
            return None

        break_flag = False
        root_index = start+1
        for post_elem in reversed(postorder):
            while (root_index > finish):
                in_elem = inorder[root_index]
                if (post_elem == in_elem):
                    root = post_elem
                    break_flag = True
                    break
            if (break_flag):
                break
        if (root is None):
            return None
        print("root", root, " at", root_index)
        print("left ", start, root_index)
        left_node = self.createNode(postorder, inorder, start, root_index)
        print("right", root_index, finish)
        right_node = self.createNode(postorder, inorder, root_index, finish)
        return TreeNode(root, left_node, right_node)


"""
- inorder prints left subtree, then value, then right subtree
- postorder prints left subtree, then right subtree, then value
- must account for missing subtrees
- last item in postorder traversal is the root
- if right subtree is null
    - both inord and postord print left then root
- if left subtree is null
    - inord prints value then right subtree, postorder prints right subtree then value



"""

if __name__ == "__main__":
    s = Solution()
    # s.largestRectangleArea(heights=[2, 1, 5, 6, 2, 3])
    s = [1, 2, 3, 4, 5]

    print(enumerate(s)[0])
