

#// Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

#// For example, a tower with 3 floors looks like this:

#// [
#//   "  *  ",
#//   " *** ", 
#//   "*****"
#// ]



#// A tower with 5 floors

#// [
#//   "    *    ",
#//   "   ***   ",
#//   "  *****  ",
#//   " ******* ",
#//   "*********",


#// ]


# create a function appends string to the list

# first string equal amount of white space

# "build a function that takes in an integer" --DK

#sean L solution:

def xmas_tree(num):
    christmas = []
    tree_height=''
    w = num*2 - 1
    for floor in range(num):
        tree = ("*" * w)
        w -= 2
        space = floor * " "
        my_tree = space + tree + space
        christmas.append(my_tree)
    christmas.reverse()
    return christmas



print(xmas_tree(3))

