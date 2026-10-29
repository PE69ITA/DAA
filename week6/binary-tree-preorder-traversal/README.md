# Binary Tree Preorder Traversal

## Approach
Used an iterative approach with a stack. Start by pushing the root node onto the stack. Pop a node, add its value to the result, then push its right child followed by its left child. This ensures the left subtree is processed first.

## Example
Input: `root = [1,null,2,3]`

Traversal:
1. Visit node `1`.
2. Push `2` onto the stack.
3. Visit node `2`, then visit its left child `3`.

Output: `[1, 2, 3]`

## Complexity
- **Time:** O(n), because each node is processed once.
- **Space:** O(n) in the worst case for the stack and result.

## Reflection
The stack allows preorder traversal without recursion. Pushing the right child before the left child is important because the stack follows LIFO order. The left child must be processed first.
