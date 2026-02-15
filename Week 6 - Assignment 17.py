'''

Challenge: Optimize the function to handle large input lists efficiently.

==============================
Description: Develop a function called find_common_elements that takes two lists as input and returns a new list containing elements that are common to both input lists.

'''

def find_common_elements(list1, list2):
    if len(list1) < len(list2):
        smaller, larger = list1, list2
    else:
        smaller, larger = list2, list1

    larger_set = set(larger)

    return [item for item in smaller if item in larger_set]
