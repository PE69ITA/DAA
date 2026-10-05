1. Problem
check if a linked list contains a cycle

2. Approach
i use two pointers slow and fast
slow moves one node at a time and fast moves two nodes at a time
if they meet there is a cycle
if fast reaches the end there is no cycle

Tracing:
3 -> 2 -> 0 -> -4

1. slow = 3, fast = 3
2. slow = 2, fast = 0
3. slow = 0, fast = 2
4. slow = -4, fast = -4
5. slow == fast -> cycle found

3. Time Complexity
O(n) both pointers move through the linked list

4. Space Complexity
O(1) only two pointers are used

5. Reflection / Improvement
the solution is already efficient in time and uses constant extra space
