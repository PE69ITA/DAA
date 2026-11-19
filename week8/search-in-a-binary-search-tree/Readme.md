# Search in a Binary Search Tree

## 1. Problem

Given the root of a binary search tree and a target value, find the node with that value and return the subtree rooted at that node. If the value does not exist, return None.

## 2. Approach

I used recursion to search for the target value. Since this is a Binary Search Tree, I only need to check one subtree at each step.

- If the current node is None, return None.
- If the current node contains the target value, return it.
- If the target is smaller, search in the left subtree.
- Otherwise, search in the right subtree.

### Example / Trace

Input: root = [4, 2, 7, 1, 3], val = 2

1. Start at node 4.
2. Since 2 < 4, move to the left child.
3. Visit node 2.
4. The target is found, so return the subtree rooted at node 2.

Output: [2, 1, 3]

### Challenges and Testing

The main thing to consider was returning the entire subtree instead of only the target value. I tested the solution with an existing value and with a value that does not exist in the tree.

## 3. Time Complexity

- Average case: O(log n), when the tree is balanced.
- Worst case: O(n), when the tree is skewed.

The algorithm visits only one branch of the tree at each step.

## 4. Space Complexity

- Average case: O(log n), due to recursive calls.
- Worst case: O(n), when the tree is skewed.

## 5. Reflection / Improvement

The solution uses the BST property to avoid checking every node. An iterative approach could eliminate recursive calls and reduce auxiliary space usage.
