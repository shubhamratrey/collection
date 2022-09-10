"""
Write a program to reverse an array or string

Given an array (or string), the task is to reverse the array/string.
Examples :


Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}

"""


def reverse_list_s2(items):
    """Time Complexity : O(n) | Recursive Way :"""

    start = 0
    end = len(items) - 1

    while start < end:
        start_val = items[start]
        end_val = items[end]
        items[start] = end_val
        items[end] = start_val
        start += 1
        end -= 1
    return items


items = [1, 2, 3, 4, 5, 6]
print(reverse_list_s2(items=items))


def reverse_list_s1(items):
    final_item = list()
    n = len(items)
    for i in range(n):
        final_item.append(items[(n - 1) - i])
    return final_item
