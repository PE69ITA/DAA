Solved in 2024

1. Problem
merge two sorted linked lists into one sorted linked list

2. Approach
i use a dummy node and a current pointer
i compare the current nodes of both lists and add the smaller one to the result
when one list ends i add the remaining part of the other list

Tracing:
list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4

1. compare 1 and 1 -> take 1 from list2
2. compare 1 and 3 -> take 1 from list1
3. compare 2 and 3 -> take 2 from list1
4. compare 4 and 3 -> take 3 from list2
5. compare 4 and 4 -> take 4 from list2
6. list2 ends -> add remaining 4 from list1

result: 1 -> 1 -> 2 -> 3 -> 4 -> 4

3. Time Complexity
O(n + m) each node from both lists is processed once

4. Space Complexity
O(1) only a few pointers are used and no new list is created

5. Reflection / Improvement
the solution is already efficient in time and uses constant extra space
