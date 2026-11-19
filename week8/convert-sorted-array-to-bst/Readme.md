# Convert Sorted Array to Binary Search Tree

## 1. Problem

Given an integer array nums where elements are sorted in ascending order, convert it into a height-balanced Binary Search Tree.

## 2. Approach

I used recursion to build the Binary Search Tree.

- Find the middle element of the current array range.
- Create a TreeNode using the middle element.
- Build the left subtree using the left half of the array.
- Build the right subtree using the right half of the array.
- Repeat until the range becomes empty.

### Example / Trace

Input: [-10, -3, 0, 5, 9]

1. Find the middle element 0. It becomes the root.
2. The left part [-10, -3] creates the left subtree.
3. The right part [5, 9] creates the right subtree.
4. Continue selecting middle elements until all elements are used.

Output: [0, -3, 9, -10, null, 5]

### Challenges and Testing

The main challenge was choosing the correct middle element and dividing the array into smaller ranges. I tested the solution with an odd-sized sorted array.

## 3. Time Complexity

O(n), because every element is visited once and used to create one tree node.

## 4. Space Complexity

O(n) for the resulting tree. The recursive call stack requires O(log n) space because the resulting tree is balanced.

## 5. Reflection / Improvement

Choosing the middle element at each step helps create a balanced BST. The recursive approach is simple and ensures that the height difference between the left and right subtrees remains minimal.
