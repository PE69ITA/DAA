# Binary Tree Postorder Traversal

## Approach
Used recursion to traverse the binary tree in postorder. First, recursively visit the left subtree, then the right subtree, and finally add the current node's value to the result.

## Example
Input: `root = [1,null,2,3]`

Traversal:
1. Visit the left subtree of `1` (empty).
2. Visit the right subtree: first `3`, then `2`.
3. Add `1` last.

Output: `[3, 2, 1]`

## Complexity
- **Time:** O(n), because each node is visited once.
- **Space:** O(n) for the result and recursion stack in the worst case.

## Reflection
Recursion makes postorder traversal simple to implement. An iterative solution using a stack could avoid recursive calls and reduce the risk of hitting Python's recursion limit for very deep trees.
