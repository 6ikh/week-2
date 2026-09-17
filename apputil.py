import numpy as np


# update/add code below ...

# defining function ways
def ways(n):
    """Returns the number of ways to make n cents using pennies and nickels"""
    # start off with counters set at 0 for ways to make change
    # also start counter for nickels at 0
    ways_count = 0
    nickels = 0
    # while the amount of nickels is less than or equal to the amount of change
    while nickels <= n:
        # add 1 to the ways count for each way to make change
        ways_count += 1
        # also add 5 to the nickels counter for each way to make change
        nickels += 5
    # return the ways count
    return ways_count


# defining function lowest_score
def lowest_score(names, scores):
    """Returns the name of the student with the lowest test score"""
    # find the index of the lowest score in the scores array
    lowest_score_index = np.argmin(scores)
    # use the lowest score index to find and return the student name
    return names[lowest_score_index]

# defining function sort_names
def sort_names(names, scores):
    """Returns the student names in descending order of test score"""
    # sort the scores in descending order and return the names in that order
    sorted_names = np.argsort(scores)[::-1]
    # return the names in the order of the sorted scores
    return [names[i] for i in sorted_names]
