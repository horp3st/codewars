#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
#For example:

    #unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    #unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    #unique_in_order([1,2,2,3,3])       == [1,2,3]

#alternative 1
def unique_in_order(iterable):

    list = []
    pose = ''

    for c in iterable:
        if c is pose:
            continue
        else:
            list.append(c)
        pose = c

    return list

print(unique_in_order('abcdeefgaab'))

#alternative 2
def unique_in_order2(iterable2):
    list2 = []
    for item in iterable2:
        if len(list2) == 0 or item != list2[-1]:
            list2.append(item)
    return list2
