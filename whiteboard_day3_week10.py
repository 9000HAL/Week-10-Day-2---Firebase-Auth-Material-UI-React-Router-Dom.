# Write a function that takes two arrays of strings as input, a1 and a2. The function should
# return an array r that contains all of the strings in a1 that are substrings of strings in a2,
# sorted in lexicographical order.
# Example 1:
# a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns ["arp", "live", "strong"]
# Example 2:
# a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns []



#KB SOLUTION: it works but problematic....re: time complexity: 

""" 
def solution(a1, a2):
    new_list = []

    for word in a1:
        for word in a2:
            if word in word1 and word not in new_list:
                new_list.append(word)
    return new_list

print(solution(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))

"""

# SEE PIC DK SOLUTION FIX + research other approaches....
