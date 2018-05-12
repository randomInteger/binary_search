#!/usr/bin/env python3.6
'''
binsearch.py

binary search on a sorted array to find a value

bin_search(numbers, value) is the real implementation

The rest is just so its easy to test with and understand.

Author:  c.gleeson 2018

Args:
1)  Int: Starting value of the range to search
2)  Int: Max value of the range to search
2)  Int: The step for the range (i.e. step by 1 or 2 or 13)
2)  Int: The value to search for inside the list created by the previous args

ex:  ./binsearch.py 0 1000 2 3
Search the list [0,2,4,6,...1000] for the value 3, will print False.

Returns:  Prints True if found and False if not found
'''
from sys import argv
from math import log2

def bin_search(numbers, value):
    '''
    inputs:
    numbers is a non empty sorted list of integers
    value is an integer value to search for

    algo:
    start with low at 0 and high at max index
    while low is less than or equal to high:
        calculate a new mid = floor (high + low / 2)
        if numbers[mid] < value
            move low up by mid + 1
        else if numbers[mid] > value
            move high down by mid - 1
        else:
            #we found the value
            return success
    return failure #we fell out without finding the value

    Returns:  A tuple of (Result, iterations) where Result is a bool and
    iterations is the number of actual iterations it took to finish.
    '''
    low_i = 0
    max_i = len(numbers) - 1
    high_i = max_i
    iterations = 0

    while low_i <= high_i:
        iterations += 1
        mid = int((high_i + low_i) / 2)
        if numbers[mid] < value:
            low_i = mid + 1
        elif numbers[mid] > value:
            high_i = mid - 1
        else:
            return (True, iterations)
    return (False, iterations)

def main():
    #Lets get some args
    try:
        minr = int(argv[1])
        maxr = int(argv[2]) + 1
        step = int(argv[3])
        value = int(argv[4])
    except IndexError as err:
        print("USAGE to search the range 1-1000, stepping by 2 for the value 33 -> ./binsearch.py 1 1000 2 33")
        raise err

    num_range = [i for i in range(minr,maxr,step)]

    #some friendly output
    print("\nRunning a binary search on a list from " + str(minr) + " to " + str(maxr-1) + " stepping by " + str(step))
    print("With search value of:", value)
    print("Number of elements in the list:", str(len(num_range)))
    expected_iterations = int(log2(len(num_range))) + 1
    print("Max possible iterations log2(len(numbers_list)) ~= ", str(expected_iterations))
    (result, iterations) = bin_search(num_range, value)
    print("Search complete after %s iterations" % (iterations))

    if result:
        print("\nFOUND: %s was found in the range!\n" % (value))
    else:
        print("\nNOT FOUND: %s was not found in the range!\n" % (value))

if __name__ == '__main__':
    main()
