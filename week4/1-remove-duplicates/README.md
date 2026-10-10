Solved in 2024

1. Problem
The task is to remove duplicate values from a sorted linked list. Each value should appear only once, and the original order must be preserved
Example: 1 -> 1 -> 2 -> 3 -> 3 becomes 1 -> 2 -> 3

2. Approach
First, I check if the list is empty. If head is None, I return. Otherwise, I create a pointer called temp that starts at the head
While temp and temp.next exist, I compare their values. If they are equal, I skip the next node by setting temp.next = temp.next.next. Otherwise, I move temp to the next node
Finally, I return head

Example / Trace
Input: 1 -> 1 -> 2 -> 3 -> 3
1. The first two values are equal, so I remove the second node: 1 -> 2 -> 3 -> 3
2. The values 1 and 2 are different, so I move temp forward
3. The values 2 and 3 are different, so I move temp forward again
4. The last two values are equal, so I remove the duplicate: 1 -> 2 -> 3
5. The loop stops because there is no next node.

Output: 1 -> 2 -> 3
Challenges and Testing
An important detail is not moving temp after removing a duplicate. The next node may have the same value, so it must be checked again

Test cases to consider:
- [1, 1, 2, 3, 3] -> [1, 2, 3]
- [1, 1, 1] -> [1]
- [1, 2, 3] -> [1, 2, 3]
- [] -> []


3. Time Complexity
O(n) - in the worst case, the algorithm traverses the entire list. Each iteration performs a constant amount of work

4. Space Complexity
O(1) - the algorithm uses only the temp pointer and does not create another list

5. Reflection / Improvement
The solution is already optimal in time and additional space complexity. Every node may need to be checked, so the time complexity is O(n), while the additional space complexity is O(1)
