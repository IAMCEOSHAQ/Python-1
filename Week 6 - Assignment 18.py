'''

Challenge: Ensure that the function works correctly with tuples of different lengths.

=============================================
Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.

'''


def concat_tuples(tuple1, tuple2):
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise TypeError("Both inputs must be tuples.")

    return tuple1 + tuple2
