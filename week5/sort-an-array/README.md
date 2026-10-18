Originally solved using Counting Sort

1. Problem

sort an array of integers in ascending order

2. Approach

i find the minimum and maximum values and create a frequency array for their range
i count how many times each number appears and rebuild the sorted array using these frequencies

Tracing:

nums = [4, 2, 2, 8, 3, 3, 1]

min_val = 1
max_val = 8

frequencies:
1: 1
2: 2
3: 2
4: 1
5: 0
6: 0
7: 0
8: 1

result = [1, 2, 2, 3, 3, 4, 8]

3. Time Complexity

O(n + k)

finding min and max and counting elements takes O(n)
iterating through the frequency array takes O(k)
rebuilding the result takes O(n)

k is the range between the minimum and maximum values

4. Space Complexity

O(n + k)

the frequency array uses O(k) space and the result array uses O(n) space

5. Reflection / Improvement

counting sort works well when the range of values is small
if the range is very large compared to the number of elements a merge sort approach can be more memory efficient
