# Minimum Depth of Binary Tree

## Approach
Used recursion to find the minimum depth. If the node is `None`, return `0`. If both children exist, return one plus the minimum depth of the two subtrees. If only one child exists, continue through that child to ensure the path reaches a leaf node.

## Example
Input: `root = [3,9,20,null,null,15,7]`

Steps:
1. Start at root `3`.
2. The left subtree reaches leaf `9` at depth `2`.
3. The right subtree reaches leaves `15` and `7` at depth `3`.
4. Return the smaller depth: `2`.

Output: `2`

## Complexity
- **Time:** O(n), because each node may need to be visited.
- **Space:** O(h) for the recursion stack, where h is the tree height. In the worst case, O(n).

## Reflection
The main challenge is handling nodes with only one child. Taking the minimum depth directly would be incorrect because a missing child is not a leaf. Checking which children exist ensures the path ends at an actual leaf.
