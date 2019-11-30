# Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
# (The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)
#
# Example:
#
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6

from collections import deque

def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    sort_arr = deque(sorted(arr))
    sort_arr.popleft()
    sort_arr.pop()
    return sort_arr