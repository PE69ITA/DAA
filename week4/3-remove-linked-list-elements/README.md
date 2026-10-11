1. Problem
The task is to remove all nodes from a linked list whose values are equal to a given value val. The function should return the head of the updated list.
Example: 1 -> 2 -> 6 -> 3 -> 6, val = 6
Output: 1 -> 2 -> 3

2. Approach
I create a dummy node called temp and connect it to the head of the original list. I use two pointers, prev and curr. The prev pointer refers to the node before the current node, while curr checks each node.
If curr.val equals val, I remove the current node by setting prev.next = curr.next. Otherwise, I move prev to curr. After each iteration, I move curr to the next node.
Finally, I return temp.next, which points to the updated list.
Example / Trace
Input: 1 -> 2 -> 6 -> 3 -> 6, val = 6

1. curr points to 1, which is not equal to 6, so prev moves to 1.
2. curr points to 2, which is not equal to 6, so prev moves to 2.
3. curr points to 6, so I skip this node by connecting 2 to 3.
4. curr points to 3, which is not equal to 6, so prev moves to 3.
5. curr points to the last 6, so I remove it.
6. The loop ends, and I return the updated list.

Output: 1 -> 2 -> 3

Challenges and Testing

The dummy node makes it easier to remove nodes at the beginning of the list without handling the head separately. Another important detail is that prev should not move when a node is removed, because the next node might also have the target value.
Test cases to consider: [1, 2, 6, 3, 6] with val = 6, [7, 7, 7] with val = 7, [1, 2, 3] with val = 4, and an empty list.

3. Time Complexity
O(n) because the algorithm visits each node once, where n is the number of nodes in the list.

4. Space Complexity
O(1) because the algorithm uses a fixed number of pointers and one dummy node, regardless of the list size.

5. Reflection / Improvement
The solution is already optimal in time complexity because every node must be checked. It also uses O(1) additional space, so no extra data structure is needed.
