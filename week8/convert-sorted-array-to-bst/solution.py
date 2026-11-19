from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(start, end):
            if start == end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = build(start, mid)
            root.right = build(mid + 1, end)
            return root
        return build(0, len(nums))

def print_tree(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result

nums = [-10, -3, 0, 5, 9]
root = Solution().sortedArrayToBST(nums)
print("Output:", print_tree(root))
