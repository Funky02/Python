# def a():
#     l=1
#     print(l)
# a()
# print(l)  # you can access only with in a function where the varaible is created
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# def a():  # x value i need to acess in fun b for that we can use 2 methods
#     x=12
# def b():
#     q=a()
#     y=2
#     print(y)
#     print(q)
# b()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def a():
    global x
    x=12
def b():
    print(x)
a()
b()
