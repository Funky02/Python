# def x(a,b,c=1):
#     print(a,b,c)
# x(1,2,c=9)

#+++++++++++++++++arbitary positional argument+++++++++++++++++++++++++++++

def y(a,b,*c):
    print(a,b,c)
y(1,2,3,4,5,6)  #*c values are assign in tuple
