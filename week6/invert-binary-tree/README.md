# Invert Binary Tree

## Approach
Used recursion to invert the binary tree. First, swap the left and right children of the current node. Then recursively invert both subtrees. If the node is `None`, return it.

## Example
Input: `root = [4,2,7,1,3,6,9]`

Steps:
1. Swap children of `4`: `2` and `7`.
2. Swap children of `2`: `1` and `3`.
3. Swap children of `7`: `6` and `9`.

Output: `[4,7,2,9,6,3,1]`

## Complexity
- **Time:** O(n), because each node is visited once.
- **Space:** O(h) for the recursion stack, where h is the height of the tree. In the worst case, O(n).

## Reflection
Recursion makes it easy to invert each subtree. Swapping the children before recursive calls ensures both subtrees are processed in their new positions. An iterative solution using a queue or stack could avoid recursion.
