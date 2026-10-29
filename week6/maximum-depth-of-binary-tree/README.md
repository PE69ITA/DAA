# Maximum Depth of Binary Tree

## Approach
Used recursion to calculate the maximum depth. For each node, recursively calculate the depth of its left and right subtrees, then return the larger value. If the node is `None`, return the current depth.

## Example
Input: `root = [3,9,20,null,null,15,7]`

Steps:
1. Start at root `3` with depth `0`.
2. The left subtree reaches node `9`, giving depth `2`.
3. The right subtree reaches nodes `20` and then `15` or `7`, giving depth `3`.
4. Return the maximum depth: `3`.

Output: `3`

## Complexity
- **Time:** O(n), because each node is visited once.
- **Space:** O(h) for the recursion stack, where h is the tree height. In the worst case, O(n).

## Reflection
Recursion simplifies finding the maximum depth by comparing the depths of both subtrees. The current depth is passed as an argument, which avoids adding one to the returned result at every recursive call.
