1. Problem
find the first bad version among versions from 1 to n

2. Approach
i check the middle version with isBadVersion() if it is bad i search the left half otherwise i search the right half

3. Time Complexity
O(log n) the number of versions to check is reduced by about half each time.
<img width="2534" height="1344" alt="image" src="https://github.com/user-attachments/assets/8cb9c638-8286-4439-8377-415f4505e019" />


4. Space Complexity
O(1) only a few variables are used

5. Reflection / Improvement
a linear search could take O(n) api calls binary search reduces this to O(log n) 
