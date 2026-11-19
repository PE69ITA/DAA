# Range Sum of BST

## 1. Problem

Given the root of a Binary Search Tree and two integers low and high, return the sum of all node values within the range [low, high].

## 2. Approach

I used Depth-First Search (DFS) with recursion to traverse the tree.

- If the current node is None, stop the recursion.
- If the node value is within the range, add it to the total sum and check both subtrees.
- If the node value is smaller than low, search only the right subtree.
- If the node value is greater than high, search only the left subtree.

### Example / Trace

Input: root = [10, 5, 15, 3, 7, null, 18], low = 7, high = 15

1. Start at node 10. Add 10 to the sum.
2. Move to node 5. Since 5 is smaller than 7, search only the right subtree.
3. Visit node 7. Add 7 to the sum.
4. Return to node 10 and move to node 15. Add 15 to the sum.
5. Visit node 18. Since 18 is greater than 15, search only the left subtree.

Output: 32

### Challenges and Testing

The main challenge was understanding how to skip unnecessary subtrees using the BST property. I tested the solution with values inside and outside the given range.

## 3. Time Complexity

O(n) in the worst case, because the algorithm may need to visit every node.

## 4. Space Complexity

O(h), where h is the height of the tree, due to recursive calls.

- Balanced BST: O(log n).
- Skewed BST: O(n).

## 5. Reflection / Improvement

The BST property allows the algorithm to skip subtrees that cannot contain values within the given range. This reduces unnecessary traversal compared to visiting every node.
