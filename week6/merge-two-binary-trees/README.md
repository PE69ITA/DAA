# Merge Two Binary Trees

## Approach
Used recursion to merge two binary trees. If both nodes exist, create a new node with the sum of their values and recursively merge their left and right subtrees. If only one node exists, return that node.

## Example
Input: `root1 = [1,3,2,5]`, `root2 = [2,1,3,null,4,null,7]`

Steps:
1. Merge roots: `1 + 2 = 3`.
2. Merge left children: `3 + 1 = 4`.
3. Merge right children: `2 + 3 = 5`.
4. Continue merging corresponding subtrees. If only one node exists, keep that subtree.

Output: `[3,4,5,5,4,null,7]`

## Complexity
- **Time:** O(n + m), where n and m are the numbers of nodes in the two trees, because each overlapping pair is processed once and remaining subtrees are returned directly.
- **Space:** O(min(h1, h2)) for the recursive calls while both nodes exist, where h1 and h2 are the tree heights. The returned tree can contain up to O(n + m) nodes.

## Reflection
Recursion makes it easy to merge corresponding nodes. Creating new nodes avoids modifying the original trees where both nodes exist. When only one node exists, the solution reuses that subtree instead of copying it.
