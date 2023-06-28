# Task
# A list S will be given. You need to generate a list T from it by following the given process:

# Remove the first and last element from the list S and add them to the list T.
# Reverse the list S
# Repeat the process until list S gets emptied.
# The above process results in the depletion of the list S. Your task is to generate list T without mutating the input List S.

# Example
# S = [1,2,3,4,5,6]
# T = []

# S = [2,3,4,5] => [5,4,3,2]
# T = [1,6]

# S = [4,3] => [3,4]
# T = [1,6,5,2]

# S = []
# T = [1,6,5,2,3,4]
# return T


# KASEY IN CLASS:
# "you could append the first and last indices to list T"

def solution(a_list):
    new_list = []

    while len(a_list) > 0:
        popped = a_list.pop(0)
        if len(a_list) > 0:
            pop_last = a_list.pop()
        a_list.reverse()
        new_list.append(popped)
        new_list.append(pop_last)

    return new_list

solution([1,2,3,4,5,6,7])





#######################################SEE DK example pic 6/27 TO STUDY HERE: