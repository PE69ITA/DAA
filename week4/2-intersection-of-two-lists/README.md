1. Problem
The task is to find the node where two singly linked lists intersect, or return None if they do not intersect. An intersection means both lists share the same node, not just nodes with equal values.

2. Approach
I use two pointers, a and b. Pointer a starts at headA, and pointer b starts at headB. Both pointers move one node forward at each iteration. When a pointer reaches the end of its list, it switches to the head of the other list. This makes both pointers travel the same total distance. The loop continues until both pointers refer to the same node. If the lists intersect, they meet at the intersection node. If they do not intersect, both pointers eventually become None.

Example / Trace

List A: 1 -> 2 -> 3 -> 7 -> 8
List B: 4 -> 5 -> 7 -> 8

Assume the nodes with values 7 and 8 are shared by both lists.
1. Pointer a starts at node 1 and pointer b starts at node 4.
2. Both pointers move forward one node at a time.
3. When a reaches the end of List A, it switches to the head of List B.
4. When b reaches the end of List B, it switches to the head of List A.
5. After switching lists, both pointers meet at the shared node with value 7.

Output: The intersection node with value 7.
Challenges and Testing
An important detail is comparing the nodes themselves using a != b instead of comparing their values. Two different nodes can have the same value without being an intersection.
Test cases to consider: two lists with a shared node, two lists that do not intersect, two empty lists, one empty list and one non-empty list, and two lists that intersect at their first node.

3. Time Complexity
O(n + m) because each pointer traverses both lists at most once, where n and m are the lengths of the two lists.

4. Space Complexity
O(1) because the algorithm uses only two pointers and does not create additional data structures.

5. Reflection / Improvement
The solution is already optimal in time and additional space complexity. It finds the intersection in O(n + m) time using O(1) additional space.
