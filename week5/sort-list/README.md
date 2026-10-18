1. Problem

sort a linked list in ascending order

2. Approach

i copy all node values into a Python list
i sort the list using the built-in sort method
then i write the sorted values back into the linked list

Tracing:

original list: 4 -> 2 -> 1 -> 3

values: [4, 2, 1, 3]

after sorting: [1, 2, 3, 4]

result: 1 -> 2 -> 3 -> 4

3. Time Complexity

O(n log n)

copying values and writing them back take O(n)
sorting the list takes O(n log n)

4. Space Complexity

O(n)

an additional list stores all node values

5. Reflection / Improvement

merge sort can sort the linked list directly without copying all values into an additional list
the time complexity remains O(n log n) and the extra space can be reduced with an in-place linked list approach
