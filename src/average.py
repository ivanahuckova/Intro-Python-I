# Returned the centered averages of array of ints,
# which we'll say is the mean average of the values,
# except ignoring the largest and the smallers values
# in the array

# User int division to produce final average
# You may assume that the list's length is 3 or more


# centered_average([1, 2, 3, 4, 100]) -> 3
# centered_average([1, 1, 5, 5, 10, 8, 7]) -> 5
# centered_average([-10, -4, -2, -4, -2, 0]) -> -3


import statistics
numbers = [1, 41, 34, 29, 50, 50]

# assume ints, has at least 3 items


def centered_average(ints):
    # create variables to hold the smallest and largest numbers
    # smallest = min(ints) -> utilize the min() function
    # largest = max(ints) -> utilize the max() function
    # set a sum to zero
    sum = 0
    # loop over all ints inside the list
    for i in ints:
        sum += i

    # remove largest and smallest number
    sum = sum - min(ints) - max(ints)
    # return the sum divided by length of the ints list - 2
    return sum / (len(ints) - 2)


print(centered_average(numbers))

# imports are not hoisted

# create a function to return the centered average using built
#  in methods of the list class and statistics module


def centered_average2(ints):
    # duplicate the list
    nums = ints.copy()
    # sort the duplicated list
    nums.sort()
    # return the centered average by using mean from the statistics module
    return statistics.mean(ints[1: -1])


print(centered_average2(numbers))
