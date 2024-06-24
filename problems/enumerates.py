#######################ENUMERATE###################################

# my_list = ['apple', 'banana', 'cherry']
# for index, value in enumerate(my_list):
#     print(index, value)


######################## REVERSE OF ENUMERATE #########################################

my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(reversed(my_list)):
    print(len(my_list) - index - 1, value)






# l=[1,2,3,4]
# def a(l):
#     return l*l

# print(list(map(a,l)))