class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.hey = 4


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.result = True
        self.traverse([], root)
        print(self.result)
        return self.result

    def traverse(self, arr, tree):
        if (not tree):
            return

        val = tree.val

        self.traverse(arr, tree.left)
        if (len(arr) > 0 and arr[-1] >= val):
            self.result = False
        arr.append(val)
        self.traverse(arr, tree.right)


"""
Post solution reflections:
    - I solved it using inorder traversing with an array. This solution has probably crossed a feat of ugliness.
        - This works because using inorder traversing to traverse the entire array guarantees a sorted array if the tree is valid.
    - It could have also been solved with DFS.
    - The empty array check was also not neccesary, could have put inifity as the first element in the array
    - Maybe the array itself was not neccesary aswell.
"""
