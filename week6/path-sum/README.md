# Path Sum

## Approach
Used recursion to check whether a root-to-leaf path equals the target sum. Subtract the current node's value from the target and recursively check both subtrees. When a leaf node is reached, check whether its value equals the remaining target. If the node is `None`, return `False`.

## Example
Input: `root = [5,4,8,11,null,13,4,7,2,null,null,null,1]`, `targetSum = 22`

Steps:
1. Start at `5`, remaining sum: `17`.
2. Visit `4`, remaining sum: `13`.
3. Visit `11`, remaining sum: `2`.
4. Visit leaf `2`, remaining sum matches its value.

Output: `True`

## Complexity
- **Time:** O(n), because each node may be visited once.
- **Space:** O(h) for the recursion stack, where h is the tree height. In the worst case, O(n).

## Reflection
Subtracting each node's value makes it easy to track the remaining sum without calculating the entire path. Checking only leaf nodes is important because the path must end at a leaf, not just any node with a matching sum.
