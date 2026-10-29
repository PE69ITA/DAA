# Sum of Left Leaves

## Approach
Used recursive DFS to calculate the sum of all left leaf nodes. If the current node is `None`, return `0`. If its left child is a leaf, add that child's value and recursively process the right subtree. Otherwise, recursively process both subtrees.

## Example
Input: `root = [3,9,20,null,null,15,7]`

Steps:
1. Start at root `3`.
2. Node `9` is a left leaf, so add `9`.
3. Visit the right subtree rooted at `20`.
4. Node `15` is a left leaf, so add `15`.
5. Node `7` is a right leaf, so do not add it.

Output: `24`

## Complexity
- **Time:** O(n), because each node is visited at most once.
- **Space:** O(h) for the recursion stack, where h is the tree height. In the worst case, O(n).

## Reflection
The main challenge is distinguishing left leaves from right leaves. Checking that the left child has no children ensures that only left leaves are added. The function can skip further traversal of a left leaf because it has no children.
