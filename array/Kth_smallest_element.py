"""
Kth the smallest element

Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth the smallest
element in the given array. It is given that all array elements are distinct.

Example 1:

Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given
array is 7.
"""

# Considering arr has
arr = [7, 10, 4, 20, 15]

# Find out third-smallest element in the given array. Let K=3
K = 4

# Sort the array list
arr.sort()

# Since position of the list starts from 0th index hence subtracting K-1 of Kth value.
p = arr[K - 1]
print(p)
