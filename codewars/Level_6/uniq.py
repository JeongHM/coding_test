# Implement a function which behaves like the uniq command in UNIX.

# It takes as input a sequence and returns a sequence in which all duplicate elements following each other have been reduced to one instance.

# Example:

# ['a','a','b','b','c','a','b','c'] --> ['a','b','c','a','b','c']


def uniq(seq):
    seq.append(True)
    answer = [seq[i] for i in range(len(seq) - 1) if seq[i] != seq[i + 1]]
    return answer




# from itertools import groupby

# def uniq(seq): 
#     return [k for k,_ in groupby(seq)]