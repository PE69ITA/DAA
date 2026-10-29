# Binary Tree Paths

## Approach
Used Depth-First Search (DFS) with recursion. Build the path by adding each node's value. When a leaf node is reached, add the complete path to the result. Otherwise, append `"->"` and recursively visit the left and right children.

## Example
Input: `root = [1,2,3,null,5]`

Traversal:
1. Start at node `1`, path: `"1"`
2. Visit node `2`, path: `"1->2"`
3. Visit leaf node `5`, add `"1->2->5"`
4. Return and visit node `3`, add `"1->3"`

Output: `["1->2->5", "1->3"]`

## Complexity
- **Time:** O(n²) in the worst case, because path strings are repeatedly concatenated and can have a length of O(n) for each node.
- **Space:** O(n²) in the worst case for stored path strings, plus O(h) recursion stack, where h is the tree height.

## Reflection
DFS makes it straightforward to build each root-to-leaf path. String concatenation can take extra time for large trees. An improvement would be to use a list to store path values and join them only when a leaf is reached.
