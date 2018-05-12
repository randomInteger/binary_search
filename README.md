# binsearch.py

binary search on a sorted array to find a value, takes args that will create a large list for testing.

Author:  c.gleeson 2018

```
Args:
1)  Int: Starting value of the range to search
2)  Int: Max value of the range to search
2)  Int: The step for the range (i.e. step by 1 or 2 or 13)
2)  Int: The value to search for inside the list created by the previous args

Example:  ./binsearch.py 0 1024 1 1024    
This example would create a list from 0 to 1024 (inclusive) stepping by 1, searching for the value 1024
and it will succeed.
```
# Note

This is a deceiving algorithm.  If you don't have the actual algorithm memorized, I highly urge you to try implementing this once, without looking at the algorithm or code at all.  

It may surprise you, how easy it is to start out with a bad approach and end up with messy code to handle all of the corner cases.

If you can get this right on the first try:  I'm not even mad, that is amazing.

I will fully admit that my first time doing this cold (no internet, no books) I made it a lot more complex than it needed to be.  This is the cleanest implementation that I have written so far.

# Example output, success:

Create a list from 0-1024 (inclusive), stepping by 1's, looking for value 1023
```
$ ./binsearch.py 0 1024 1 1023

Running a binary search on a list from 0 to 1024 stepping by 1
With search value of: 1023
Number of elements in the list: 1025
Max possible iterations log2(len(numbers_list)) ~=  11
Search complete after 10 iterations

FOUND: 1023 was found in the range!
```

Create a list from 0-1024 (inclusive), stepping by 3's, looking for value 999
```
$ ./binsearch.py 0 1024 3 999

Running a binary search on a list from 0 to 1024 stepping by 3
With search value of: 999
Number of elements in the list: 342
Max possible iterations log2(len(numbers_list)) ~=  9
Search complete after 7 iterations

FOUND: 999 was found in the range!
```

# Example output, failure:

Create a list from 0-10 (inclusive), stepping by 1's, looking for value -1
```
$ ./binsearch.py 0 10 1 -1

Running a binary search on a list from 0 to 10 stepping by 1
With search value of: -1
Number of elements in the list: 11
Max possible iterations log2(len(numbers_list)) ~=  4
Search complete after 3 iterations

NOT FOUND: -1 was not found in the range!
```

Create a list from 0-10000 (inclusive), stepping by 1's, looking for value 10002
```
$ ./binsearch.py 0 10000 1 10002

Running a binary search on a list from 0 to 10000 stepping by 1
With search value of: 10002
Number of elements in the list: 10001
Max possible iterations log2(len(numbers_list)) ~=  14
Search complete after 14 iterations

NOT FOUND: 10002 was not found in the range!
```
