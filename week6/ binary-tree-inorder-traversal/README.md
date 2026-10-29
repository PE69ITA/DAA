# Binary Tree Inorder Traversal

## Approach
Used an iterative approach with a stack instead of recursion. First, traverse as far left as possible and push each node onto the stack. Then pop a node, add its value to the result, and move to its right subtree. Repeat until both the current node and stack are empty.

## Example
Input: `root = [1, null, 2, 3]`

Traversal:
1. Visit the leftmost node: `1`
2. Move to the right subtree and visit `3`
3. Visit `2`

Output: `[1, 3, 2]`

## Complexity
- **Time:** O(n), because each node is pushed and popped from the stack once.
- **Space:** O(n), because the stack can store up to n nodes in the worst case.

## Reflection
The iterative approach avoids recursion and its call stack. The main challenge was managing when to move left, pop a node, and then move right.
