Merge Sort is an efficient sorting algorithm that sorts data by continuously dividing the input into smaller subarrays 
and then merging those subarrays in sorted order. It guarantees consistent performance even for large datasets.


ALGORITHM:
MergeSort(arr)

1. If array contains one element
       Return

2. Find the middle index.

3. Divide array into
       Left Half
       Right Half

4. Recursively apply MergeSort on
       Left Half
       Right Half

5. Merge both sorted halves.


TIME COMPLEXITY:
The time complexity in worst and the best case remains the same i.e O(n log n)
SPACE COMPLEXITY:
The space complexity is O(n)
