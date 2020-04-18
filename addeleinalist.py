my_list = [3,4,56,2,1]
len_list = len(my_list)
my_range = range(0,len_list)
print(my_range)
new_list = list(range(0,5))
print(new_list)

# Writing a function to add all elements in a list

#first attempt
def list1(num):

    total = 0
    for x in num:
        total = total + x
    return total

print(list1([2,3,5,2]))

#second attempt
