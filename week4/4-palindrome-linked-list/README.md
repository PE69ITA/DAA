1. Problem
The task is to check whether a singly linked list is a palindrome, meaning its values read the same forward and backward
Example: 1 -> 2 -> 2 -> 1 returns True, while 1 -> 2 returns False

2. Approach
I create an empty list called ans and use a pointer curr to traverse the linked list
While curr is not None, I append the value of each node to ans and move curr to the next node
After collecting all values, I compare ans with ans[::-1], which creates a reversed copy of the list
If both lists are equal, the linked list is a palindrome and the function returns True, otherwise it returns False

Example / Trace

Input: 1 -> 2 -> 2 -> 1

1. Start with an empty list: ans = []
2. Visit the first node and append 1: ans = [1]
3. Visit the second node and append 2: ans = [1, 2]
4. Visit the third node and append 2: ans = [1, 2, 2]
5. Visit the last node and append 1: ans = [1, 2, 2, 1]
6. Reverse the list and compare: [1, 2, 2, 1] == [1, 2, 2, 1]

Output: True

Challenges and Testing

An important detail is using ans[::-1] to create a reversed copy of the list for comparison

Test cases to consider: [1, 2, 2, 1] returns True, [1, 2] returns False, [1] returns True, and an empty list returns True

3. Time Complexity
O(n) because the algorithm traverses all n nodes and then compares the collected values with their reversed copy, which also takes linear time

4. Space Complexity
O(n) because the ans list stores the value of every node, and reversing it creates another list of the same size

5. Reflection / Improvement
A more space-efficient approach is to find the middle of the linked list, reverse the second half, and compare both halves
This approach can achieve O(n) time complexity and O(1) additional space complexity
