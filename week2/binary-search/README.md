1. Problem
find the index of a target value in a sorted array. Return -1 if the target is not found

2. Approach
i compare the target with the middle element and remove half of the search range each time

3. Time Complexity
time Complexity: O(log n) after each iteration, the search range is approximately divided by two therefore, the number of elements that need to be checked grows logarithmically with the size of the array.
<img width="2369" height="1126" alt="image" src="https://github.com/user-attachments/assets/83738eef-d5d6-4d2f-a5b5-24983b4c3ecd" />

4. Space Complexity
Space Complexity: O(1), algorithm only uses a few variables such as low, high, and mid and it does not create another array or use additional data structures

5. Reflection / Improvement
Bbinary search is already efficient for a sorted array and a linear search would take O(n), while this solution takes O(log n)
