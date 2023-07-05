from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        leng = len(nums)
        if leng == 1:
            return TreeNode(nums[0], left=None, right=None)

        return self.createTree(nums, 0, leng-1)

    def createTree(self, arr, start, end):
        if (start == end+1):
            return None
        mid = (start + end)//2

        left = self.createTree(arr, start, mid-1)
        right = self.createTree(arr, mid+1, end)

        return TreeNode(arr[mid], left=left, right=right)


if __name__ == "__main__":
    s = Solution()
    s.sortedArrayToBST(nums=[2, 1, 5, 6, 2, 3])
