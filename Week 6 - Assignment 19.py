'''

Challenge: Implement the sorting algorithm without using any built-in sorting functions.

====================================
Description: Develop a function called sort_list that takes a list of numbers as input and returns a new list containing the same elements sorted in ascending order.

'''


def sort_list(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")

    # Base case
    if len(numbers) <= 1:
        return numbers[:]

    # Divide
    mid = len(numbers) // 2
    left = sort_list(numbers[:mid])
    right = sort_list(numbers[mid:])

    # Conquer (merge step)
    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list
